import requests
from dotenv import load_dotenv
import os
import json
import sys




load_dotenv()
key = os.environ['TAIWANCWA_KEY']
dataid = 'F-D0047-069'
locationname = '板橋區'
elementname = ['天氣預報綜合描述', '舒適度指數', '3小時降雨機率', '體感溫度']
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/'




params = {'Authorization': key, 'LocationName': locationname, 'ElementName': elementname}
res = requests.get(URL+dataid, params=params, verify=False).json()

for weatherelement in res['records']['Locations'][0]['Location'][0]['WeatherElement']:
    for time in weatherelement['Time']:
        print(time)
        print(f'{'':=>30}')


    