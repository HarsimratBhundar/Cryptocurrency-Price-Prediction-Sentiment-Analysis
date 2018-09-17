import requests
import json
import os
import pandas as pd

apiurl = 'https://api.coindesk.com/v1/bpi/'

def get_price_data(url, type, from_date, to_date):
	prices = requests.get(url + type + '.json?start=' + from_date + '&end=' + to_date).json()['bpi']
	data = pd.DataFrame(data=prices, index = [0]).T
	data.reset_index(level=0, inplace=True)
	data.columns = ['date', 'price']
	data['date'] = data['date'].apply(lambda x: str(x).replace('-', '.'))
	return data


df = get_price_data(apiurl, 'historical/close', '2017-12-01', '2018-09-02')
df.to_csv(os.path.join(os.path.dirname(__file__), "data/dat.csv"))

