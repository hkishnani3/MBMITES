from Google_api_function_2 import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = 'db_py.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
gsheetId = '1x_iX2FT55beqqWcasvh4sB0dBJ2c4Y2Rj9cuhrSiYPc'

s = Create_Service(CLIENT_SECRET_FILE,API_SERVICE_NAME,API_VERSION,SCOPES)
gs = s.spreadsheets()
rows = gs.values().get(spreadsheetId = gsheetId , range = 'processed_data').execute()
data = rows.get('values')
df = pd.DataFrame(data)
print(df)
