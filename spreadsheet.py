import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("ubuntu saving").get_worksheet(2)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
file = open("data.json", "w")
with file as fout:
    json.dump(list_of_hashes, fout)
file.close()
