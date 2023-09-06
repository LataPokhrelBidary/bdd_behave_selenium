from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helper.SeleniumHelper import SeleniumHelper
from Locators import locators
from Logs import logs

log = logs.get_logs()

login_url= "https://www.facebook.com/"
@when('user enter incorrect user name "{user_name}" and password "{password}"')
def enter_cred(context, user_name, password):
    SeleniumHelper(context.driver).open_url(login_url)
    log.info("url opened")
    SeleniumHelper(context.driver).insert_text(locators.input_field_login, user_name)
    SeleniumHelper(context.driver).insert_text(locators.input_field_password, password)
    SeleniumHelper(context.driver).click_login(locators.button_login)
    log.info("login button clicked")

@then('error message should be displayed')
def error_msg(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login/identify')]"))
        )
        print("test passed")
    except:
        print("test failed")
