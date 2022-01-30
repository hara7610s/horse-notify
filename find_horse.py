import time

def scrape_list(driver,url):

    driver.get(url)
    elements = driver.find_elements_by_class_name('HorseList')
    row = []

    for element in elements:
        horsenames = element.find_elements_by_class_name('HorseName')

        for horsename in horsenames:
            title = horsename.find_element_by_tag_name('a').get_attribute('title')
            row.append(title.encode("utf-8"))
        
    time.sleep(1)
    driver.close()
    
    return row
