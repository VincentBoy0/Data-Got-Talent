import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

categories = ['Sáng','Trưa','Chiều','Tối']
file_path = 'data.xlsx'

df = pd.read_excel(file_path, sheet_name = 'ticket',dtype={'saledate':str,'date':str,'time':str})

sang = ({'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]})
trua = ({'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]})
chieu = ({'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]})
toi = ({'ticketcode':[],'saledate':[],'date':[],'time':[],'room':[],'film':[]})
indexColumn = ['ticketcode','saledate','date','time','room','film']
indexCol = [5,2,6,7,9,10]

def get(initialData, addData, indexRow):
    for item in indexColumn:
        addData[item].append(initialData[item].values[indexRow])

def cal(T):
    Tmp = ''
    for i in T:
        if i == ':':
            break
        Tmp += i
    Tmp = int(Tmp)
    if Tmp >= 7 and Tmp <= 11:
        return 0
    if Tmp > 11 and Tmp < 15:
        return 1
    if Tmp >= 15 and Tmp < 19:
        return 2
    if Tmp >= 19 and Tmp <= 24:
        return 3

row_size = df['time'].size
for i in range(row_size):
    if cal(str(df['time'][i])) == 0:
        get(df,sang,i)
    elif cal(str(df['time'][i])) == 1:
        get(df,trua,i)
    elif cal(str(df['time'][i])) == 2:
        get(df,chieu,i)
    else:
        get(df,toi,i)

print(sang)
print(trua)
print(chieu)
print(toi)

sang = pd.DataFrame(sang)
trua = pd.DataFrame(trua)
chieu = pd.DataFrame(chieu)
toi = pd.DataFrame(toi)
fileName = "idea3Analysis.xlsx"

with pd.ExcelWriter(fileName, engine='xlsxwriter') as writer:
    sang.to_excel(writer,sheet_name='Sáng (7h-11h)',index = False)
    trua.to_excel(writer,sheet_name='Trưa (12h-14h)',index = False)
    chieu.to_excel(writer,sheet_name = 'Chiều (15h-18h)',index = False)
    toi.to_excel(writer,sheet_name='Tối (19h-24h)',index = False)

