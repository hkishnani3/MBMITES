# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 23:23:14 2020

@author: hkish

from google sheets to pandas dataframe
"""
COM_PORT = 'COM13'

from Google_api_function_2 import Create_Service
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import serial
from time import sleep


CLIENT_SECRET_FILE = 'db_py.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
gsheetId = '1CkvGDr58kpDX-SFV1xrd0o_d5Xt8KP2lR-js34DJa4A'

s = Create_Service(CLIENT_SECRET_FILE,API_SERVICE_NAME,API_VERSION,SCOPES)
gs = s.spreadsheets()
rows = gs.values().get(spreadsheetId = gsheetId , range = 'Sheet1!A2:B23').execute()
data = rows.get('values')
df = pd.DataFrame(data)

""" data is a 2-D array with Lists as entry 'Temperature', 'Coefficient of thermal expansion' so needs to be converted to int - type list"""
df[1] = pd.to_numeric(df[1],downcast='float') 

df[1] = df[1].apply(lambda x: 1.e-6*x)

df[0] = pd.to_numeric(df[0],downcast='signed')
print(df)
#plt.plot(df[0] , df[1],'b^')
#plt.title("Coefficient of thermal expansion v/s Temperature")


coeff_LC = np.polyfit(df[0],df[1],1)
Y_LC = np.polyval(coeff_LC, df[0])
#plt.plot(df[0] ,Y_LC ,'r--')


coeff_QC = np.polyfit(df[0],df[1],2)
Y_QC = np.polyval(coeff_QC, df[0])
#plt.plot(df[0] ,Y_QC ,'g--')


coeff_CC = np.polyfit(df[0],df[1],3)
Y_CC = np.polyval(coeff_CC, df[0])
#plt.plot(df[0] ,Y_CC ,'c--')

#plt.show()

#----connect to arduino via serial-------------------------------------------------------------
ser = serial.Serial(COM_PORT,baudrate = 9600)
count_min = 0
while True:
    count_min+=1
    ser.write(count_min)
    print(ser.readline().decode('ascii'))
    sleep(1)