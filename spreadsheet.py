import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_spreadsheet():
    # authorize gspread
    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcp_secret.json", scope)
    client = gspread.authorize(creds)

    # get all values as list of lists
    sheet = client.open("horse_DB").sheet1
    mylists = sheet.get_all_values()
    
    # make dictionary with encoding
    mylist_utf8 =[]
    for mylist in mylists:
        mylist_utf8.append(list(map(lambda s:s.encode("utf-8"), mylist)))
    
    mydict = {}
    for l in mylist_utf8:
        mydict[l[0]] = l[1:]


    return mydict

