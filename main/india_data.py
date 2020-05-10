# import requests
# from django.shortcuts import render
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
