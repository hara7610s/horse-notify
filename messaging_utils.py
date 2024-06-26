import time

import os
import requests
LINE_NOTIFY_TOKEN = os.environ["LINE_NOTIFY_TOKEN"]

def post_message(message):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"
    }
    data = {
        "message": message
    }
    requests.post(
        url,
        headers=headers,
        data=data
    )


def search_and_notify_entry(entry_dict, my_dict):
    for my_horse in my_dict:
        if my_horse in list(entry_dict.keys()):
            RaceCourse = entry_dict[my_horse][0].decode('utf-8')
            RaceNum = entry_dict[my_horse][1].decode('utf-8')
            RaceName = entry_dict[my_horse][2].decode('utf-8')
            HorseName = my_horse.decode('utf-8')
            comments = my_dict[my_horse]
            text = ''
            for comment in comments:
                if comment.decode('utf-8') != '':
                    text = text + '\n' + comment.decode('utf-8')
                else:
                    break
            
            post_message(f'\n{RaceCourse}{RaceNum} {RaceName}\n{HorseName}{text}')
            time.sleep(2)