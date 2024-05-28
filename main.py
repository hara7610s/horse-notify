import line
import datetime

import checking_entry
from scraping_utils import spreadsheet, get_race_list, find_horses

def main():
    # find race pages tomorrow
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    race_id_list = get_race_list(tomorrow)
    
    # make a list of horses entered tomorrow
    if len(race_id_list) == 0:
        pass
    else:
        entry_dict = {}
        for race_id in race_id_list:
            each_race = find_horses(race_id)

            entry_dict.update(each_race)

        # call my horse list
        my_dict = spreadsheet.read_spreadsheet()

        line.notify_message(tomorrow)
        
        # match entry list and my horse list
        checking_entry.notify_entry(entry_dict, my_dict)

if __name__ == "__main__":
    main()
