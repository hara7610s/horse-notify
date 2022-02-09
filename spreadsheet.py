import gc
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

type = str(os.environ["TYPE"])
project_id = str(os.environ["PROJECT_ID"])
private_key_id = str(os.environ["PRIVATE_KEY_ID"])
private_key = str(os.environ["PRIVATE_KEY"])
client_email = str(os.environ["CLIENT_EMAIL"])
client_id = str(os.environ["CLIENT_ID"])
auth_uri = str(os.environ["AUTH_URI"])
token_uri = str(os.environ["TOKEN_URI"])
auth_provider_x509_cert_url = str(os.environ["AUTH_PROVIDER_X509_CERT_URL"])
client_x509_cert_url = str(os.environ["CLIENT_X509_CERT_URL"])

def read_spreadsheet():
    gcp_secret = {
        'type':type,
        'project_id':project_id,
        'private_key_id':private_key_id,
        'private_key':private_key,
        'client_email':client_email,
        'client_id':client_id,
        'auth_uri':auth_uri,
        'token_uri':token_uri,
        'auth_provider_x509_cert_url':auth_provider_x509_cert_url,
        'client_x509_cert_url':client_x509_cert_url
        }
    
    gcp_secret['private_key'] = gcp_secret['private_key'].replace('\\n', '\n')

    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(gcp_secret, scope)
    client = gspread.authorize(creds)

    sheet = client.open("horse_DB").sheet1

    return sheet.col_values(1)

