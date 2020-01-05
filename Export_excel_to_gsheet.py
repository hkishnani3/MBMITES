# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:20:02 2020

@author: hkish
"""
from Google_api_function_2 import Create_Service
import win32com.client as win32

#Excel part-----------------------------------------------------------------------------------------
xlApp = win32.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(r"C:\Users\hkish\.spyder-py3\Export_excel_to_gsheet_file.xlsx")
ws = wb.Worksheets('Sheet1')
rngData = ws.Range('A1').CurrentRegion()


#Google Sheet part----------------------------------------------------------------------------------
gsheetId = '1lJ5e4tMqazSNZqgBecma841r13aKojnPASr-tLtBc0M'
CLIENT_SECRET_FILE = 'db_py.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service = Create_Service(CLIENT_SECRET_FILE,API_SERVICE_NAME,API_VERSION,SCOPES)


response = service.spreadsheets().values().append(
    spreadsheetId = gsheetId,
    valueInputOption = 'RAW',
    range = 'Sheet_1!A1',
    body = dict(
        majorDimension = 'ROWS',
        values = rngData
    )
).execute()


