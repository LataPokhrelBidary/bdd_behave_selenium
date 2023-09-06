from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def insert_text(self, locator, input_text):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)
    def click_login(self, locator):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()

    def wait_till_element_error_check(self, locator, timeout=10):
        flag = False
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            flag = True
        except Exception as e:
            print(f"Element {list(locator.values())[0]} not found after waiting {timeout} seconds")
        return flag