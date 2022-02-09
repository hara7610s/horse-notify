import gc
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_spreadsheet():
    json_open = open("./config/gcp_secret.json", "r")
    gcp_secret = json.load(json_open)

    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("./config/gcp_secret.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("horse_DB").sheet1

    return sheet.col_values(1)

