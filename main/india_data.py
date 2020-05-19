import requests
#
# def indian_data():
#     url = 'https://api.covid19india.org/data.json'
#
#     response = requests.get(url).json()
#     statewise_response = response['statewise']
#
#     all_state_data = []
#     for data in statewise_response:
#         state = data['state']
#         active = data['active']
#         confirmed = data['confirmed']
#         deaths = data['deaths']
#         recovered = data['recovered']
#
#         # above returns VALUE as a string from state KEY
#         # creating key value pair of all strings to an individual key
#         datas = {
#             'state': state,
#             'active': active,
#             'confirmed': confirmed,
#             'deaths': deaths,
#             'recovered': recovered
#         }
#         # [{}, {}, {}]
#         all_state_data.append(datas)
#
#     for state in all_state_data:
#         print(state['confirmed'])
#     # expected dict to be returned & stored in the context var inside index fnc
#     #return {'all_state_data': all_state_data[1:]}
#
#
# indian_data()

#
url = 'https://api.covid19india.org/resources/resources.json'
response = requests.get(url).json()

resource = response['resources']
print(resource)
all_resource = []
for res in resource:
    all_resource.append(res)

    # doing this because we want few keys out of whole keys
    # category = res['category']
    # city = res['city']
    # contact = res['contact']
    # description = res['descriptionandorserviceprovided']
    # state = res['state']

    # above all return values (here string) associated to the keys

    # datas = {
    #     'category': category,
    #     'city': city,
    #     'contact': contact,
    #     'state': state,
    #     'description': description
    # }
    # # now we assign each value to a key & loop goes on
print(all_resource)
