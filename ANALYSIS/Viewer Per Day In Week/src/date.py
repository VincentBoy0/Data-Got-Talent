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
value = [0,0,0,0,0,0,0];
Money = [0,0,0,0,0,0,0];
for j in range(len(df.slot)):
    i = df['date'][j];
    Ngay = i.to_pydatetime();
    Ngay = str(Ngay);    
    value[Date1[Cal(Ngay)]] += 1;
    Money[Date1[Cal(Ngay)]] += df['ticket price'][j];
    
    
#### Draw ####
fig, axs = plt.subplots(2, 1, figsize = (15, 7))
axs[0].set_title('Viewers per day in week(%)')
axs[0].pie(value,labels = categories, autopct='%1.1f%%')
axs[1].set_title('Salary per day in week(%)')
axs[1].pie(Money,labels = categories, autopct='%1.1f%%')
plt.show()