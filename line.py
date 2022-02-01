import os
import requests
LINE_NOTIFY_TOKEN = os.environ["LINE_NOTIFY_TOKEN"]

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
