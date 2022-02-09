import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

type = os.environ["TYPE"]
project_id = os.environ["PROJECT_ID"]
private_key_id = os.environ["PRIVATE_KEY_ID"]
private_key = os.environ["PRIVATE_KEY"]
client_email = os.environ["CLIENT_EMAIL"]
client_id = os.environ["CLIENT_ID"]
auth_uri = os.environ["AUTH_URI"]
token_uri = os.environ["TOKEN_URI"]
auth_provider_x509_cert_url = os.environ["AUTH_PROVIDER_X509_CERT_URL"]
client_x509_cert_url = os.environ["CLIENT_X509_CERT_URL"]

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

    scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(gcp_secret, scope)
    client = gspread.authorize(creds)

    sheet = client.open("horse_DB").sheet1

    return sheet.col_values(1)

