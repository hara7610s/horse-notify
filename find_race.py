from selenium import webdriver

from get_chrome_driver import GetChromeDriver

get_driver = GetChromeDriver()
get_driver.install()
 
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
 
    driver = webdriver.Chrome(options=options)
 
    return driver

def get_race(driver, page):
    driver.get(page)
    count = len(driver.find_elements_by_id("RaceTopRace"))

    if count > 0:
        return "found"
    else:
        return "NIL"
