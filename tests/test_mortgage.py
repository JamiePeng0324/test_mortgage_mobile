import pytest
import allure
from pages.mortgage_page import MortgagePage

@allure.feature("房貸試算")
@allure.title("P1 - 正常流程：試算成功")
@allure.description("此測試驗證用戶填寫正確資料後，能正常取得試算結果")
def test_full_flow(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁"):
        page.open_url()
    with allure.step("選擇城市與行政區"):
        page.select_city("台北市")
        page.select_district("大安區")
    with allure.step("填寫金額、貸款年限與利率"):
        page.fill_amount("5")
        page.select_loan_term(20)
        page.fill_interest("7.5")
    with allure.step("執行試算"):
        page.tap_calculate()
    with allure.step("驗證試算結果是否顯示"):
        if "試算結果" not in page.get_result_text():
            allure.attach(body=page.get_result_text(), name="result text", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("未顯示試算結果")

@allure.feature("房貸試算")
@allure.title("P1 - 未填利率")
@allure.description("此測試驗證未填寫利率時，是否會出現必填提示")
def test_missing_interest(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並填寫金額與年限"):
        page.open_url()
        page.select_city("新北市")
        page.select_district("三重區")
        page.fill_amount("3")
        page.select_loan_term(20)
    with allure.step("執行試算（不填利率）"):
        page.tap_calculate()
    with allure.step("驗證錯誤提示"):
        if "*為必填欄位" not in page.need_info_text():
            pytest.fail("未顯示必填欄位提示")

@allure.feature("房貸試算")
@allure.title("P2 - 輸入過大金額")
@allure.description("此測試驗證輸入異常大金額時，系統是否有提示最大可貸金額")
def test_large_amount(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並輸入過大金額"):
        page.open_url()
        page.select_city("桃園縣")
        page.select_district("中壢市")
        page.fill_amount("99999999")
        page.select_loan_term(30)
        page.fill_interest("3.0")
    with allure.step("執行試算"):
        page.tap_calculate()
    with allure.step("驗證提示文字"):
        if "最高可貸款" not in page.get_result_text():
            pytest.fail("未顯示超過貸款額度提示")

@allure.feature("房貸試算")
@allure.title("P2 - 重設功能")
@allure.description("此測試驗證點擊重設按鈕後，輸入欄位是否被清空")
def test_reset_function(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並填寫金額"):
        page.open_url()
        page.fill_amount("12345")
    with allure.step("點擊重設"):
        page.tap_reset()
    with allure.step("驗證金額已清除"):
        if "12345" in page.get_result_text():
            pytest.fail("重設後金額未清空")

@allure.feature("房貸試算")
@allure.title("P3 - 僅選城市未選行政區")
@allure.description("此測試驗證未選擇行政區時，系統是否提示欄位為必填")
def test_missing_district(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並只選城市"):
        page.open_url()
        page.select_city("新北市")
        page.fill_amount("40000")
        page.select_loan_term(20)
        page.fill_interest("5.0")
    with allure.step("執行試算（不選行政區）"):
        page.tap_calculate()
    with allure.step("驗證錯誤提示"):
        if "*為必填欄位" not in page.need_info_text():
            pytest.fail("未顯示必填欄位錯誤")

@allure.feature("房貸試算")
@allure.title("P3 - 空白送出")
@allure.description("此測試驗證空白送出表單時，是否提示所有欄位為必填")
def test_empty_submit(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並直接試算"):
        page.open_url()
        page.tap_calculate()
    with allure.step("驗證空白提示"):
        if "*為必填欄位" not in page.need_info_text():
            pytest.fail("空白送出未提示錯誤")

@allure.feature("房貸試算")
@allure.title("P3 - 負數利率")
@allure.description("此測試驗證填寫負值利率時，是否有正確提示錯誤")
def test_negative_interest(driver):
    page = MortgagePage(driver)
    with allure.step("打開網頁並填寫負利率"):
        page.open_url()
        page.select_city("新北市")
        page.select_district("新店區")
        page.fill_amount("60000")
        page.select_loan_term(20)
        page.fill_interest("-2.5")
    with allure.step("執行試算"):
        page.tap_calculate()
    with allure.step("驗證錯誤提示"):
        if "利率不能為負" not in page.get_result_text():
            pytest.fail("未提示利率不能為負")