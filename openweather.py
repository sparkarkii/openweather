import requests
import datetime
from os import environ
import sys
sys.path.append('./my_utilities')
from my_utilities import emailfun




key = os.environ['OPENWEATHER_KEY']




def get_weather(city):
    '''
    {
    'coord': {'lon': 121.4657, 'lat': 25.012}, 
    'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 
    'base': 'stations', 
    'main': {'temp': 301.76, 'feels_like': 307.02, 'temp_min': 301.76, 'temp_max': 301.76, 'pressure': 1003, 'humidity': 81, 'sea_level': 1003, 'grnd_level': 987}, 
    'visibility': 10000, 
    'wind': {'speed': 3.49, 'deg': 95, 'gust': 7.57}, 
    'rain': {'1h': 0.27}, 
    'clouds': {'all': 0}, 
    'dt': 1786993811, 
    'sys': {'country': 'TW', 'sunrise': 1787002157, 'sunset': 1787048835}, 
    'timezone': 28800, 
    'id': 1670029, 
    'name': 'Banqiao District', 
    'cod': 200
    }
    '''

    lat, lon = get_coordinates(city)
    API = 'https://api.openweathermap.org/data/2.5/weather?'

    params = {'lat':lat, 'lon':lon, 'appid':key}
    res = requests.get(API, params=params).json()

    subject, content = format_email(res)
    emailfunc.send_email(subject=subject, content=content)




def get_coordinates(city) -> tuple[int, int]:
    '''
    [{'name': 'New Taipei', 
    'local_names': {'hr': 'Novi Taipei', 'et': 'Xinbei', 'vi': 'Tân Bắc', 'uk': 'Новий Тайбей', 'de': 'Neu-Taipeh', 'sr': 'Нови Тајпеј', 'ru': 'Новый Тайбэй', 'es': 'Nuevo Taipéi', 'sl': 'Novi Tajpej', 'th': 'ซินเป่ย์', 'cs': 'Nová Tchaj-pej', 'ar': 'تايبيه الجديدة', 'ko': '신베이 시', 'ja': '新北市', 'nl': 'Nieuw Taipei', 'pl': 'Nowe Tajpej', 'id': 'Kota Taipei Baru', 'zh': '新北市', 'tr': 'Yeni Taipei', 'fr': 'Nouveau Taipei', 'el': 'Νέα Ταϊπέι', 'pt': 'Nova Taipé', 'eu': 'Taipei Berria', 'he': 'טאיפיי החדשה', 'it': 'Nuova Taipei', 'en': 'New Taipei'}, 
    'lat': 25.011997, 
    'lon': 121.4656619, 
    'country': 'TW'}]
    '''

    API = 'http://api.openweathermap.org/geo/1.0/direct?'

    params = {'q':city, 'appid':key}
    res = requests.get(API, params=params).json()[0]
    
    return res['lat'], res['lon']




def format_email(res) -> tuple[str, str]:
    today = datetime.date.today()
    subject = f'{today}: {res['weather'][0]['description']}'
    li = []
    for k, i in res.items():
        li.append(f'{k} -> {i}')
    content = '\n'.join(li)
    return subject, content




if __name__ == '__main__':
    get_weather(city='New Taipei')
