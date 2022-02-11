import line
import find_race
import find_horse
import datetime
import spreadsheet

def main():
    today = datetime.date.today()

    kaisai_date = today + datetime.timedelta(days=1)
 
    race_list_page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + kaisai_date.strftime('%Y%m%d')
    race_list = find_race.get_race(race_list_page)

    horse_list = []

    for race in race_list:
        url = "https://race.netkeiba.com/race/shutuba.html?race_id=" + race
        each_race = find_horse.scrape_list(url)

        horse_list += each_race

    my_horses = spreadsheet.read_spreadsheet()

    horse_list_set = set(horse_list)
    my_horses_set = set(my_horses)
    entry_list = list(horse_list_set & my_horses_set)
    line.notify_message(entry_list)

if __name__ == "__main__":
    main()
