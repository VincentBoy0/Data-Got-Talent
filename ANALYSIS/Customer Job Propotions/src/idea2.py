import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Film = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='film')
Ticket = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='ticket')
Customer = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='customer')
AvailableFilm = pd.read_excel('DATA SET - VÒNG 1 CUỘC THI DATA GOT TALENT 2023.xlsx', sheet_name='film_available')

type_film = []

def list_type_film(arr):
    ans = []
    js = {}
    for i in range(len(arr)):
        tmp = arr[i].split(', ')
        for item in tmp:
            if item not in ans:
                js[item] = len(ans)
                ans.append(item)
    
    return [ans, js]

def film_type_connect(data):
    json = {}
    for i in range(len(data.title)):
        title = data.title[i]
        listed_in = data.listed_in[i].split(', ')
        json[title] = listed_in
    
    return json

[type_film, id_type_film] = list_type_film(AvailableFilm.listed_in)
list_type_of_film = film_type_connect(AvailableFilm)

def make_json_cusid(data):
    json = {}
    job_customer = []
    json_job_custonmer = {}
    for i in range(len(data.customerid)):
        id = data.customerid[i]
        json[id] = data.job[i]
        if data.job[i] not in job_customer:
            json_job_custonmer[data.job[i]] = len(job_customer)
            job_customer.append(data.job[i])
    return [json, job_customer, json_job_custonmer]

[cus_id, cus_job, json_cus_job] = make_json_cusid(Customer)
cnt_type_through_customer = np.zeros((len(cus_job), len(type_film)))

def count_type_film_appear(data):
    cnt = np.zeros(len(type_film))
    total = 0
    for i in range(len(data.slot)):
        film = data.film[i]
        if film not in list_type_of_film:
            continue

        id_job = json_cus_job[cus_id[data.customerid[i]]]
        types = list_type_of_film[film]
        for j in range(len(types)):
            cnt[id_type_film[types[j]]] += 1
            cnt_type_through_customer[id_job][id_type_film[types[j]]] += 1
            total += 1

    for j in range(len(type_film)):
        sum = 0
        for i in range(len(cus_job)):
            sum += cnt_type_through_customer[i][j]
        for i in range(len(cus_job)):
            cnt_type_through_customer[i][j] /= sum
            cnt_type_through_customer[i][j] *= 100
    return cnt

cnt_type = count_type_film_appear(Ticket)

#<-------- draw chart ------------>
fig, axs = plt.subplots(2, 1, figsize = (15, 7))
axs[0].bar(type_film, cnt_type)
axs[0].tick_params(axis='both', labelsize=7)
axs[0].set_title('The count of individuals viewing movies in each type of film')


bot = np.zeros(len(type_film))
for i in range(len(cus_job)):
    axs[1].bar(type_film, cnt_type_through_customer[i], bottom = bot, label = cus_job[i])
    bot += cnt_type_through_customer[i]
axs[1].legend()
axs[1].tick_params(axis='both', labelsize=7)
axs[1].set_title('The percentages of film genre based on different customer segments')
plt.show()