import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

categories = ['Sáng','Trưa','Chiều','Tối']
value = [0,0,0,0]

file_path = 'data.xlsx'
df = pd.read_excel(file_path, sheet_name = 'ticket')

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
for i in range(df['time'].size):
    if cal(str(df['time'][i])) == 0:
        value[0] += 1
    elif cal(str(df['time'][i])) == 1:
        value[1] += 1
    elif cal(str(df['time'][i])) == 2:
        value[2] += 1
    else:
        value[3] += 1

plt.pie(value,labels = categories, autopct='%1.1f%%',textprops={'fontsize': 25})
plt.title('Movie Watching Time Statistics',fontsize = 30, fontweight = 'bold')
plt.show()