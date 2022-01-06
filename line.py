import json
import requests
with open("line.json") as token_file:
    line_json = json.load(token_file)
LINE_NOTIFY_TOKEN = line_json["LINE_NOTIFY_TOKEN"]

def notify_message(message):
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
