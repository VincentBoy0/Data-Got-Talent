import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#<------------- File Data --------------->
Film = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='film')
Ticket = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='ticket')
Customer = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='customer')
AvailableFilm = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='film_available')

# <-------make json 'customerid': ['DOB', 'gender', 'address', 'job']------------>
cus_info = {}
for i in range(len(Customer.customerid)):
    id = Customer.customerid[i]
    dob = Customer.DOB[i]
    gende = Customer.gender[i]
    address = Customer.address[i]
    job = Customer.job[i]
    cus_info[id] = [dob, gende, address, job]

#print(cus_info)

# <----- make json 'film': 'listed_in'-------------->
tag_film = {}
for i in range(len(AvailableFilm.title)):
    title = AvailableFilm.title[i]
    type_film = AvailableFilm.listed_in[i]
    tag_film[title] = type_film

#print(tag_film)

type_customer = []
for job in Customer.job:
    if job not in type_customer:
        type_customer.append(job)
with pd.ExcelWriter('new sheet.xlsx') as writer:
    for job in type_customer:
        arr = []
        for i in range(8):
            arr.append([])

        for i in range(len(Ticket.ticketcode)):
            cusid = Ticket.customerid[i]
            info = cus_info[cusid]
            if info[3] != job:
                continue
            ticketcode = Ticket.ticketcode[i]
            film = Ticket.film[i]
            type_film = tag_film[film]
            arr[0].append(cusid)
            for j in range(4):
                arr[j+1].append(info[j])
            arr[5].append(ticketcode)
            arr[6].append(film)
            arr[7].append(type_film)

        #print(arr)
        data = {
            'customerid': arr[0],
            'DOB': arr[1],
            'gender': arr[2],
            'address': arr[3],
            'ticketcode': arr[5],
            'film': arr[6],
            'listed_in': arr[7]
        }
        df = pd.DataFrame(data)
        #print(link)
        df.to_excel(writer, sheet_name=str(job), index=False)
