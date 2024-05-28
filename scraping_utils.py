import time
import re

import bs4
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import driver_init
from selenium.webdriver.common.by import By


def read_spreadsheet():
    # authorize gspread
    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcp_secret.json", scope)
    client = gspread.authorize(creds)

    # get all values as list of lists
    sheet = client.open("horse_DB").sheet1
    myhorse_list = sheet.get_all_values()
    
    # make dictionary with encoding
    myhorse_list_utf8 =[]
    for myhorse in myhorse_list:
        myhorse_list_utf8.append(list(map(lambda s:s.encode("utf-8"), myhorse)))
    
    myhorse_dict = {}
    for l in myhorse_list_utf8:
        myhorse_dict[l[0]] = l[1:]

    return myhorse_dict


def get_race_list(date):
    page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + date.strftime('%Y%m%d')
    
    driver = driver_init.driver_init()
    driver.get(page)
    count = len(driver.find_elements(By.ID, "RaceTopRace"))

    race_list =[]

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
                        race_list.append(item_id)
        
        time.sleep(1)
        driver.quit()

        return race_list

    else:
        driver.quit()
        return race_list


def find_horses(race_id):
    url = "https://race.netkeiba.com/race/shutuba.html?race_id=" + race_id
    
    driver = driver_init.driver_init()
    driver.get(url)

    RaceCourse = driver.find_element(By.CLASS_NAME, 'RaceKaisaiWrap').find_element(By.CLASS_NAME, 'Active').find_element(By.TAG_NAME, 'a').text
    RaceNum = driver.find_element(By.CLASS_NAME, 'RaceNum').text
    RaceName = driver.find_element(By.CLASS_NAME, 'RaceName').text

    RaceInfo = [RaceCourse.encode('utf-8'), RaceNum.encode('utf-8'), RaceName.encode('utf-8')]

    elements = driver.find_elements(By.CLASS_NAME, 'HorseList')
    entry_dict = {}

    for element in elements:
        horsenames = element.find_elements(By.CLASS_NAME, 'HorseName')

        for horsename in horsenames:
            title = horsename.find_element(By.TAG_NAME, 'a').get_attribute('title')
            entry_dict[title.encode("utf-8")] = RaceInfo
        
    time.sleep(1)
    driver.quit()
    
    return entry_dict
