import bs4
import re

def get_race(driver, page):
    driver.get(page)
    count = len(driver.find_elements_by_id("RaceTopRace"))

    if count > 0:
        info = []
        
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

        return info

    else:
        return "NIL"
