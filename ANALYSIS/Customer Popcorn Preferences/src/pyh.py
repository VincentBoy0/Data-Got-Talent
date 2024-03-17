import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



file_path = 'Data.xlsx'

df = pd.read_excel(file_path,sheet_name = 'ticket')

def Cal(T):
    Tmp = '';
    for i in T:
        if i == ':':
            break;
        Tmp += i;
    Tmp = int(Tmp);
    if Tmp >= 7 and Tmp <= 11:
        return 0;
    if Tmp > 11 and Tmp < 15:
        return 1;
    if Tmp >= 15 and Tmp < 19:
        return 2;
    if Tmp >= 19 and Tmp <= 24:
        return 3;
        
pcno = 0;
pcyes = 0;
pre = '';
PotenCusPer = 0;
PotenCusGro = 0;
cnt = 0;
Sang = 0;
Trua = 0;
Chieu = 0;
Toi = 0;
categories = ['Viewers do not buy corn alone','Viewers do not buy corn in groups','Corn buyers']
value = [0,0,0]
for i in range(len(df.slot)):
    pop = df.popcorn[i];
    id = df.customerid[i];
    Total = df.total[i];
    TicPrice = df['ticket price'][i];
    if id != pre:
        cnt = 0;
    if(pop == 'Không'):
        if id == pre:
            if cnt == 0:
                PotenCusGro += 1;
                PotenCusPer += 2;
            else:
                PotenCusPer += 1;
            cnt += 1;
        pcno += 1;
    else:
        pcyes += 1;
    pre = id;

value[0] = pcno - PotenCusPer;
value[1] = PotenCusPer;
value[2] = pcyes;
plt.title('Percentage of people buying popcorn(%)')
plt.pie(value,labels = categories, autopct='%1.1f%%')
plt.show()    

print(pcno);
print(pcyes);
print(PotenCusPer);
print(PotenCusGro);
