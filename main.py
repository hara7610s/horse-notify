import line
import driver_init
import find_race
import find_horse
import datetime
import spreadsheet

def main():
    today = datetime.date.today()

    kaisai_date = today + datetime.timedelta(days=2)
 
    driver = driver_init.driver_init()
 
    race_list_page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + kaisai_date.strftime('%Y%m%d')
    race_list = find_race.get_race(driver, race_list_page)

    horse_list = []

    for race in race_list:
        driver = driver_init.driver_init()
        url = "https://race.netkeiba.com/race/shutuba.html?race_id=" + race
        each_race = find_horse.scrape_list(driver, url)

        horse_list += each_race

    driver.quit()

    line.notify_message(horse_list)

    my_horses = spreadsheet.read_spreadsheet()
    line.notify_message(my_horses)

    horse_list_set = set(horse_list)
    my_horses_set = set(my_horses)
    entry_list = list(horse_list_set & my_horses_set)
    line.notify_message(entry_list)

if __name__ == "__main__":
    main()
