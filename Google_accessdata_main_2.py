from Google_api_function_2 import Create_Service
import pandas as pd
import numpy as np

CLIENT_SECRET_FILE = 'db_py.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1x_iX2FT55beqqWcasvh4sB0dBJ2c4Y2Rj9cuhrSiYPc'

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def Export_Data_To_Sheets():
    URL = r'https://files.digital.nhs.uk/publicationimport/pub20xxx/pub20188/ccg-pres-data-oct-dec-2015-un-dat.csv'
    df = pd.read_csv(URL)
    df.replace(np.nan, '', inplace=True)

    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='processed_data!A1',
        body=dict(
            majorDimension='ROWS',
            values=df.T.reset_index().T.values.tolist())
    ).execute()

Export_Data_To_Sheets()