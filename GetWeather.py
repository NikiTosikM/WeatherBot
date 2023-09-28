from main_dates import API_WEATHER
from pprint import pprint
import requests
import whisper
import os
from aiogram import types
from datetime import datetime
from aiogram import types


async def get_weather(city, api):

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

async def get_city_from_voice(message: types.Message):

    from WeatherBot import bot

    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, 'voice/user_voice.wav')

    model = whisper.load_model("small")
    voice_user_path = r'voice\user_voice.wav'
    city_voice = model.transcribe(voice_user_path)

    symbols = {',': None, '.': None, ' ': None, ';': None}
    translate_symbols = str.maketrans(symbols)

    result_city = city_voice['text'].translate(translate_symbols)

    os.remove(r'voice\user_voice.wav')

    return result_city




