from newsapi import NewsApiClient
import json
import os
import pandas as pd
import requests
from datetime import timedelta, date
from textblob import TextBlob
from dateutil import parser

# replace your api key with '#############' in the following line of code
newsapi = NewsApiClient(api_key='#############')

def get_articles(topic, channels, date):
    return newsapi.get_everything(q=topic,
                                  sources=channels,
                                  from_param=date,
                                  to=date,
                                  language='en',
                                  sort_by='relevancy')

def get_sent_analysis(topic, channels, from_date, to_date):
    results = pd.DataFrame()
    
    for date in pd.date_range(from_date, to_date):
        print(date.strftime('%Y.%m.%d'))
        all_articles = get_articles(topic, channels, date.strftime('%Y-%m-%d'))
        results = results.append(pd.DataFrame(all_articles['articles']))

    results['polarity'] = results.apply(lambda x: TextBlob(str(x['description'])).sentiment.polarity, axis = 1)
    results['subjectivity'] = results.apply(lambda x: TextBlob(str(x['description'])).sentiment.subjectivity, axis = 1)
    results['date'] = results.apply(lambda x: parser.parse(x['publishedAt']).strftime('%Y.%m.%d'), axis = 1)
    results['time'] = results.apply(lambda x: parser.parse(x['publishedAt']).strftime('%H:%M'), axis = 1)
    
    return results.groupby(by = 'date').mean()


df = get_sent_analysis('bitcoin', 'bbc-news, the verge, financial-times, reuters, metro, cointelegraph, crypto-coins-news, bloomberg, cnbc, business-insider, google-news, forbes, fortune', date(2017,12,1), date(2018,9,10))
df.to_csv(os.path.join(os.path.dirname(__file__), "data/dat.csv"))

