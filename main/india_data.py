import requests

def indian_state_wise_data():
    url = 'https://api.covid19india.org/data.json'

    response = requests.get(url).json()

    state_wise = response['statewise']


    all = []
    for data in state_wise:
        state = data['state']
        active = data['active']
        recovered = data['recovered']
        deaths = data['deaths']

        datas = {
            'state': state,
            'active': active,
            'recovered': recovered,
            'deaths': deaths
            }
        all.append(datas)
    print(all[0])

        #print(state) # returns string ie all state names (values) of state key
    context = {'all': all[1:]}
    print(context)

indian_state_wise_data()

