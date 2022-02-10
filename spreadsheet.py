import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_spreadsheet():

    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcp_secret.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("horse_DB").sheet1
    mylist = sheet.col_values(1)
    mylist_utf8 = list(map(lambda s:s.encode("utf-8"), mylist))

    return mylist_utf8

