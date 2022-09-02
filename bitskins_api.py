import urllib.request
from urllib.parse import quote
import json
import pyotp
import pandas as pd

class bitskins:

#initialise api key and secret
    def __init__(self):
        self.API_KEY = 'API_KEY HERE'
        self.my_secret = 'SECRET GOES HERE'

#Retrieve bitskins sale data for specific Market Hash(only logs 6 pgs of data)

    def get_bitskins_data(self,MARKET_HASH_NAME):

        my_token = pyotp.TOTP(self.my_secret)
        CODE = my_token.now()


        for PAGE in range (1,6):
            url = 'https://bitskins.com/api/v1/get_sales_info/?api_key={}&code={}&market_hash_name={}&page={}&app_id=APP_ID'.format(self.API_KEY,CODE,MARKET_HASH_NAME,PAGE)
            json_obj = urllib.request.urlopen(url)
            data_bitskins = json.load(json_obj)

            return data_bitskins



#Retrieve steam sale data for specific Market Hash
    def get_steam_data(self,MARKET_HASH_NAME):

        my_token = pyotp.TOTP(self.my_secret)
        CODE = my_token.now()

        url = 'https://bitskins.com/api/v1/get_steam_price_data/?api_key={}&market_hash_name={}&app_id=730&code={}'.format(self.API_KEY,MARKET_HASH_NAME,CODE)
        json_obj = urllib.request.urlopen(url)
        data_steam = json.load(json_obj)
        
        return data_steam

