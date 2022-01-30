from selenium import webdriver
from get_chrome_driver import GetChromeDriver

get_driver = GetChromeDriver()
get_driver.install()
 
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
 
    driver = webdriver.Chrome(options=options)
 
    return driver