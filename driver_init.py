from selenium import webdriver
from get_chrome_driver import GetChromeDriver
from selenium.webdriver.common.by import By

get_driver = GetChromeDriver()
get_driver.install()
 
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
 
    driver = webdriver.Chrome(options=options)
 
    return driver