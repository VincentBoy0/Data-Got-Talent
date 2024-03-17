import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



file_path = 'Data.xlsx'

df = pd.read_excel(file_path,sheet_name = 'ticket')

def Cal(Ngay):
    cnt = 0;
    s = '';
    for j in Ngay:
        if j == '-':
            cnt += 1;
            continue;
        if cnt == 2:
            s = s + j;
        if j == ' ':
            break;
    s = int(s);
    return s % 7;

Date1 = [1, 2, 3, 4, 5, 6, 0];
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Thu2 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
Thu3 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
Thu4 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
Thu5 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
Thu6 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
Thu7 = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
CN = ({'orderid':[],'cashier':[], 'ticket price':[],'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]});
ID = ({'orderid','cashier', 'ticket price','ticketcode','saledate','date','time','room','film'});

def get(initialData, addData, indexRow):
    for item in ID:
        addData[item].append(initialData[item].values[indexRow])
value = [0,0,0,0,0,0,0];
Money = [0,0,0,0,0,0,0];
for j in range(len(df.slot)):
    i = df['date'][j];
    Ngay = i.to_pydatetime();
    Ngay = str(Ngay);    
    if Date1[Cal(Ngay)] == 0:
        get(df,Thu2,j);
    elif Date1[Cal(Ngay)] == 1:
        get(df,Thu3,j);
    elif Date1[Cal(Ngay)] == 2:
        get(df,Thu4,j);
    elif Date1[Cal(Ngay)] == 3:
        get(df,Thu5,j);
    elif Date1[Cal(Ngay)] == 4:
        get(df,Thu6,j);
    elif Date1[Cal(Ngay)] == 5:
        get(df,Thu7,j);
    elif Date1[Cal(Ngay)] == 6:
        get(df,CN,j);
Thu2 = pd.DataFrame(Thu2);
Thu3 = pd.DataFrame(Thu3);
Thu4 = pd.DataFrame(Thu4);
Thu5 = pd.DataFrame(Thu5);
Thu6 = pd.DataFrame(Thu6);
Thu7 = pd.DataFrame(Thu7);
CN = pd.DataFrame(CN);
fileName = "idea5Analysis.xlsx"

with pd.ExcelWriter(fileName, engine='xlsxwriter') as writer:
    Thu2.to_excel(writer,sheet_name='Thu2',index = False)
    Thu3.to_excel(writer,sheet_name='Thu3',index = False)
    Thu4.to_excel(writer,sheet_name='Thu4',index = False)
    Thu5.to_excel(writer,sheet_name='Thu5',index = False)
    Thu6.to_excel(writer,sheet_name='Thu6',index = False)
    Thu7.to_excel(writer,sheet_name='Thu7',index = False)
    CN.to_excel(writer,sheet_name='CN',index = False)