import time
import bs4
import re
import driver_init
from selenium.webdriver.common.by import By

def get_race_list(date):
    page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + date.strftime('%Y%m%d')
    
    driver = driver_init.driver_init()
    driver.get(page)
    count = len(driver.find_elements(By.ID, "RaceTopRace"))

    info =[]

    if count > 0:
        source = driver.page_source
        soup = bs4.BeautifulSoup(source, 'lxml')

        elem_base = soup.find(id="RaceTopRace")
 
        if elem_base:
            elems = elem_base.find_all("li", class_="RaceList_DataItem")
 
            for elem in elems:
                a_tag = elem.find("a")
 
                if a_tag:
                    href = a_tag.attrs['href']
                    match = re.findall("..\/race\/shutuba.html\?race_id=(.*)&rf=race_list", href)
 
                    if len(match) > 0:
                        item_id = match[0]
                        info.append(item_id)
        
        time.sleep(1)
        driver.quit()

        return info

    else:
        driver.quit()
        return info

