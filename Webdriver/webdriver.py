from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_driver():
    driver = webdriver.Chrome(service=Service("C:\\Users\\anilb\\OneDrive\\Desktop\\chromedriver.exe"))
    return driver

