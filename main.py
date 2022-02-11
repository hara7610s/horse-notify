import line
import find_race
import find_horse
import datetime
import spreadsheet

def main():
    # find race pages tomorrow
    today = datetime.date.today()
    kaisai_date = today + datetime.timedelta(days=1)
    race_list_page = "https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=" + kaisai_date.strftime('%Y%m%d')
    race_list = find_race.get_race(race_list_page)
    
    # make a list of horses entered tomorrow
    horse_list = []

    for race in race_list:
        url = "https://race.netkeiba.com/race/shutuba.html?race_id=" + race
        each_race = find_horse.scrape_list(url)

        horse_list += each_race

    # match entry list and my horse list
    my_dict = spreadsheet.read_spreadsheet()

    for my_horse in my_dict:
        if my_horse in horse_list:
            message = [my_horse, my_dict[my_horse]]
            line.notify_message(message)

if __name__ == "__main__":
    main()
