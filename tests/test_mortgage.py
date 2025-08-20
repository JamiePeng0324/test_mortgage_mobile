import pytest
import allure
import time
from pages.mortgage_page import MortgagePage

@allure.feature("Mortgage Calculator")
@allure.story("P1 - 正常流程")
def test_full_flow(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.select_city("台北市")
    page.select_district("大安區")
    page.fill_amount("5")
    page.select_loan_term("20年")
    page.fill_interest("7.5")
    page.tap_calculate()
    time.sleep(5)
    assert "試算結果" in page.get_result_text()

@allure.story("P1 - 未填利率")
def test_missing_interest(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.select_city("新北市")
    page.select_district("三重區")
    page.fill_amount("3")
    page.select_loan_term("20年")
    page.tap_calculate()
    time.sleep(5)
    assert "*為必填欄位" in page.get_result_text()

@allure.story("P2 - 輸入過大金額")
def test_large_amount(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.select_city("桃園縣")
    page.select_district("中壢市")
    page.fill_amount("99999999")
    page.select_loan_term("30年")
    page.fill_interest("3.0")
    page.tap_calculate()
    time.sleep(5)
    assert "最高可貸款" in page.get_result_text()

@allure.story("P2 - 重設功能")
def test_reset_function(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.fill_amount("12345")
    page.reset_form()
    time.sleep(5)
    assert "12345" not in page.get_result_text()

@allure.story("P3 - 僅選城市不選行政區")
def test_missing_district(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.select_city("新北市")
    page.fill_amount("40000")
    page.select_loan_term("20年")
    page.fill_interest("5.0")
    page.tap_calculate()
    time.sleep(5)
    assert "*為必填欄位" in page.need_info_text()

@allure.story("P3 - 空白送出")
def test_empty_submit(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.tap_calculate()
    time.sleep(5)
    assert "*為必填欄位" in page.need_info_text()

@allure.story("P3 - 負數利率")
def test_negative_interest(driver):
    page = MortgagePage(driver)
    page.open_url()
    page.select_city("新北市")
    page.select_district("新店區")
    page.fill_amount("60000")
    page.select_loan_term("20年")
    page.fill_interest("-2.5")
    page.tap_calculate()
    time.sleep(5)
    assert "利率不能為負" in page.get_result_text()