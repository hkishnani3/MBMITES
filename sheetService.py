import pickle
import os
from pprint import pprint as pp
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pandas as pd

CLIENT_SECRET_FILE = 'db_py.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

cred = None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        cred = pickle.load(token)

if not cred or not cred.valid:
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
        
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE,SCOPES)
        cred = flow.run_local_server()
    
    with open('token.pickle','wb') as token:
        pickle.dump(cred, token)

try:
    service = build(API_SERVICE_NAME,API_VERSION, credentials = cred)
    print('Service created successfully')
    print(service)
except Exception as e:
    print(e)