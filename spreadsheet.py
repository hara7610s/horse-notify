import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_spreadsheet():

    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcp_secret.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("horse_DB").sheet1
    #get all values as list of lists
    mylists = sheet.get_all_values()
    
    mylist_utf8 =[]
    for mylist in mylists:
        mylist_utf8.append(list(map(lambda s:s.encode("utf-8"), mylist)))
    
    mydict = dict(mylist_utf8)

    return mydict

