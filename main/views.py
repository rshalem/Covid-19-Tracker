import requests
from django.shortcuts import render
import datetime


d = datetime.datetime.now()
def home(request):


    # timeline is the resource
    url = 'https://corona-api.com/timeline'


    response = requests.get(url, timeout=2).json()

    # # news api

    values = {
        "confirmed": response['data'][0]['confirmed'],
        "recovered": response['data'][0]['recovered'],
        "deaths": response['data'][0]['deaths'],
        "per_increase": ((response['data'][0]['confirmed']-response['data'][1]['confirmed'])
                              /(response['data'][0]['confirmed'])*100),
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

def news(request):

    news_url = 'https://newsapi.org/v2/everything?q=COVID&from=d&sortBy=publishedAt&' \
               'apiKey=66c90e23bb0443b8ae9594cd66fc7817&pageSize=10&page=1'
    news_response = requests.get(news_url).json()
    article = news_response['articles']


    all_news = []

    # article contains list of dictionaries
    # we need to loop over it to get single-single dictionary
    # from that single article we're gonna fetch the value corresponding that key
    # t, u, & i contains all the values
    # in all variable, we will create a key for those fetched values & pass them in as a context

    for single_article in article:
        t = single_article['title']
        u = single_article['url']
        i = single_article['urlToImage']

        all = {
            "t": t,
            "u": u,
            "i": i,
        }

        all_news.append(all)

    context = {'all_news': all_news}
    return render(request, 'news.html', context=context)


def country_detail(request, name):
    url = 'https://covid19.mathdro.id/api/countries/'+ name
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


    return render(request, 'country_detail.html', {'country_data':country_data})


