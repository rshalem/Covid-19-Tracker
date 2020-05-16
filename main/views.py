import requests
from django.shortcuts import render

def index(request):

    # function calling, whose return values are contexts(dict)
    all_cases = world_cases()
    country_cases = country_wise_cases()
    all_news = news()
    all_indian_data = indian_data()

    # context as a dict, functions as **kwargs
    context = dict(all_cases, **country_cases, **all_news, **all_indian_data)
    return render(request, 'index.html', context=context)


# below are the individual functions for diff section of content, returning all data as a dictionary value
def world_cases():

    # timeline is the resource
    url = 'https://corona-api.com/timeline'
    response = requests.get(url).json()

    increase = round(((response['data'][0]['confirmed'] - response['data'][1]['confirmed'])
     / (response['data'][0]['confirmed']) * 100), 2)

    values = {
        "confirmed": response['data'][0]['confirmed'],
        "recovered": response['data'][0]['recovered'],
        "deaths": response['data'][0]['deaths'],
        "per_increase": increase
    }

    return {'values': values}

def country_wise_cases():

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

    return {'all_data': all_data[1:]}

def indian_data():
    url = 'https://api.covid19india.org/data.json'

    response = requests.get(url).json()
    statewise_response = response['statewise']

    all_state_data = []
    for data in statewise_response:
        state = data['state']
        active = data['active']
        confirmed = data['confirmed']
        deaths = data['deaths']
        recovered = data['recovered']

        # above returns VALUE as a string from state KEY
        # creating key value pair of all strings to an individual key
        datas = {
            'state': state,
            'active': active,
            'confirmed': confirmed,
            'deaths': deaths,
            'recovered': recovered
        }
        # [{}, {}, {}]
        all_state_data.append(datas)

    # expected dict to be returned & stored in the context var inside index fnc
    return {'all_state_data': all_state_data[1:], 'total': all_state_data[0]}

def news():

    news_url = 'https://cryptic-ravine-96718.herokuapp.com/'
    news_response = requests.get(news_url).json()
    article = news_response['news']

    all_news = []
    # article contains list of dictionaries
    # we need to loop over it to get single-single dictionary
    # from that single article we're gonna fetch the value corresponding that key
    # t, u, & i contains all the values
    # in all variable, we will create a key for those fetched values & pass them in as a context

    for single_article in article:
        t = single_article['title']
        u = single_article['link']
        i = single_article['img']

        all = {
            "t": t,
            "u": u,
            "i": i,
        }
        all_news.append(all)

    return {'all_news': all_news}


def country_detail(request, name):

    """
    :param request:
    :param name:
    :return:
    """

    url = 'https://covid19.mathdro.id/api/countries/' + name
    response = requests.get(url).json()


    country_confirm = response['confirmed']
    country_recover = response['recovered']
    country_death = response['deaths']

    confirm = country_confirm['value']
    recover = country_recover['value']
    death = country_death['value']

    country_data = {
        "confirm": confirm,
        "recovered": recover,
        "deaths": death
    }

    return render(request, 'country_detail.html', {'country_data': country_data})