import requests
from django.shortcuts import render
#
# def indian_state_wise_data():
#     url = 'https://api.covid19india.org/data.json'
#
#     response = requests.get(url).json()
#
#     state_wise = response['statewise']
#     all = []
#     for data in state_wise:
#         state = data['state']
#         active = data['active']
#         recovered = data['recovered']
#         deaths = data['deaths']
#
#         datas = {
#             'state': state,
#             'active': active,
#             'recovered': recovered,
#             'deaths': deaths
#             }
#         all.append(datas)
#     print(all)
#     #return all
#
# indian_state_wise_data()

# def country():
#
#     url = 'https://covid19.mathdro.id/api/confirmed'
#     response = requests.get(url).json()
#
#     all_data = []
#     for item in response:
#         name = item['combinedKey']
#         confirmed = item['confirmed']
#         recovered = item['recovered']
#         deaths = item['deaths']
#         active = item['active']
#
#
#         # {'name': [all names list], 'confirmed': [confirmed list], etc}
#         # .split returns a list
#         new_name = name.split(",", "")
#
#         total = {
#              'name': new_name[0],
#              "confirmed": confirmed,
#              "recovered": recovered,
#              "deaths": deaths,
#              "active": active,
#         }
#         all_data.append(total)
#
#     print(all_data)
#
#     #all_data = [item['combinedKey'] for item in response]
#
#     #return {'all_data': all_data}
#
# h = country()