import time
import driver_init

def make_entry_dict(url):
    driver = driver_init.driver_init()
    driver.get(url)

    RaceDay = driver.find_element_by_id('RaceList_DateList').find_element_by_class_name('Active').get_attribute('title')
    RaceCourse = driver.find_element_by_class_name('RaceKaisaiWrap').find_element_by_class_name('Active').find_element_by_tag_name('a').text
    RaceNum = driver.find_element_by_class_name('RaceNum').text
    RaceName = driver.find_element_by_class_name('RaceName').text

    RaceInfo = [RaceDay.encode('utf-8'), RaceCourse.encode('utf-8'), RaceNum.encode('utf-8'), RaceName.encode('utf-8')]

    elements = driver.find_elements_by_class_name('HorseList')
    dict = {}

    for element in elements:
        horsenames = element.find_elements_by_class_name('HorseName')

        for horsename in horsenames:
            title = horsename.find_element_by_tag_name('a').get_attribute('title')
            dict[title.encode("utf-8")] = RaceInfo
        
    time.sleep(1)
    driver.quit()
    
    return dict
