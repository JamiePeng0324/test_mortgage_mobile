from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MortgagePage:
    CITY_XPATH = {
        "台北市": '//*[@id="cityLtv"]/option[3]',
        "新北市": '//*[@id="cityLtv"]/option[4]',
        "桃園縣": '//*[@id="cityLtv"]/option[5]',
    }
    DISTRICT_XPATH = {
        "大安區": '//*[@id="areaLtv"]/option[4]',
        "三重區": '//*[@id="areaLtv"]/option[4]',
        "新店區": '//*[@id="areaLtv"]/option[23]',
        "中壢市": '//*[@id="areaLtv"]/option[5]',
    }

    def __init__(self, driver):
        self.driver = driver
        self.amount_input = '//*[@id="txtAmount"]'
        self.interest_input = '//*[@id="txtInterestRate"]'
        self.loan_term_year_input = '//*[@id="txtLoanTermOtherYear"]'
        self.calculate_button = '//*[@id="btnCalculate"]'
        self.reset_button = '//*[@id="btnReset"]'
        self.result_label = '//*[@id="divResult"]/section/div/div/div[1]'
        self.need_info = '//*[@id="mainform"]/div[4]/main/div/div[3]/section/div/div[1]'
        self.city_dropdown = '//*[@id="cityLtv"]'
        self.district_dropdown = '//*[@id="areaLtv"]'

    def open_url(self, url='https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-budget/'):
        self.driver.get(url)

    def select_city(self, city_name):
        self.driver.find_element(By.XPATH, self.city_dropdown).click()
        city_xpath = self.CITY_XPATH.get(city_name)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, city_xpath))
        )
        self.driver.find_element(By.XPATH, city_xpath).click()

    def select_district(self, district_name):
        self.driver.find_element(By.XPATH, self.district_dropdown).click()
        district_xpath = self.DISTRICT_XPATH.get(district_name)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, district_xpath))
        )
        self.driver.find_element(By.XPATH, district_xpath).click()

    def fill_amount(self, amount):
        self.driver.find_element(By.XPATH, self.amount_input).send_keys(amount)

    def fill_interest(self, rate):
        self.driver.find_element(By.XPATH, self.interest_input).send_keys(rate)

    def fill_loan_term_year(self, years):
        self.driver.find_element(By.XPATH, self.loan_term_year_input).send_keys(years)

    def tap_calculate(self):
        self.driver.find_element(By.XPATH, self.calculate_button).click()

    def tap_reset(self):
        self.driver.find_element(By.XPATH, self.reset_button).click()

    def need_info_text(self):
        return self.driver.find_element(By.XPATH, self.need_info).text

    def get_result_text(self):
        return self.driver.find_element(By.XPATH, self.result_label).text
