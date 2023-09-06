from Webdriver import webdriver

def before_scenario(context, scenario):
        print("edge driver launched")
        context.driver = webdriver.get_chrome_driver()
        context.driver.maximize_window()

def after_scenario(context, scenario):
        print("edge driver closed")
        context.driver.close()