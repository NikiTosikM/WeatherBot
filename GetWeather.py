from main_dates import API_WEATHER
from pprint import pprint
import requests
from datetime import datetime
from aiogram import types


def get_weather(city, api):

    try:
        weather_dates = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&lang=ru&units=metric')
        dates = weather_dates.json()

        time = str(datetime.now().time())
        now_time = ':'.join(time.split(':')[:-1])
        name_city = dates['name']
        weather_city = dates['weather'][0]['description']
        temp_average = int(dates['main']['temp_max'] + dates['main']['temp_min']) // 2

        conclusion_dates = f"{'*'*10} {now_time} {'*'*10}\nГород - {name_city}\nПогода - {weather_city}\nТемпература - {temp_average}°"

        return conclusion_dates, True
    
    except Exception as e:
        return  'Неверные данные , повторите запрос', False

def request_weather(city):

    return get_weather(city, API_WEATHER)
