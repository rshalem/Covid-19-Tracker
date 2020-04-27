import requests
from django.shortcuts import render


def home(request):

    # timeline is the resource
    url = 'https://corona-api.com/timeline'
    response = requests.get(url).json()

    values = {
        "confirmed": response['data'][0]['confirmed'],
        "recovered": response['data'][0]['recovered'],
        "deaths": response['data'][0]['deaths'],
        "per_increase": ((response['data'][0]['confirmed']-response['data'][1]['confirmed'])
                              /(response['data'][0]['confirmed'])*100)
    }

    return render(request, 'index.html', {'values': values})

def country(request):

    url = 'https://covid19.mathdro.id/api/confirmed'
    response = requests.get(url).json()

    all_data = []
    for item in response:
        name = item['combinedKey']
        confirmed = item['confirmed']
        recovered = item['recovered']
        deaths = item['deaths']
        active = item['active']

        # {'name': [all names list], 'confirmed': [confirmed list], etc}
        total = {
             'name': name,
             "confirmed": confirmed,
             "recovered": recovered,
             "deaths": deaths,
             "active": active,
        }
        all_data.append(total)

    #all_data = [item['combinedKey'] for item in response]

    context = {'all_data': all_data}
    return render(request, 'country_view.html', context=context)

def country_detail(request, name):
    pass
