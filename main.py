import line
import find_race
import datetime

def main():
    today = datetime.date.today()

    kaisai_date = today + datetime.timedelta(days=1)
 
    driver = find_race.driver_init()
 
    page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + kaisai_date.strftime('%Y%m%d')

    message = find_race.get_race(driver, page)

    line.notify_message(message)

    driver.quit()


if __name__ == "__main__":
    main()
