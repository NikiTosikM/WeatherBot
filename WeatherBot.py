import asyncio
from aiogram import Bot, types, Dispatcher, executor
import tracemalloc
from main_dates import TOKEN_BOT , API_WEATHER
from GetWeather import get_weather
from Keyboard import keyboard_buttons
from GetWeather import get_city_from_voice, get_weather



bot = Bot(token=TOKEN_BOT) 
dp = Dispatcher(bot) 

@dp.message_handler(commands=['start'])
async def start_bot (message: types.Message):
    await message.answer('Если хотите получить самую свежую информацию по погоде, то пишите название города , а остальное я сделаю все сам')

@dp.message_handler()
async def weather_city(message: types.Message):
    dates, check = await get_weather(message.text, API_WEATHER)

    keyboard = keyboard_buttons(message.text, check)

    await message.answer(dates, reply_markup= keyboard )

@dp.message_handler(content_types=types.ContentType.VOICE)
async def weather_voice(message: types.Message):

    await message.answer('Подождите... идет распознавание текста ')

    gif_image = open('images\_s_tarelkami_gif_yapfiles.ru.gif', 'rb')

    await bot.send_animation(chat_id=message.from_user.id, animation=gif_image)

    city_voice = await get_city_from_voice(message)

    city_weather, check = await get_weather(city_voice, API_WEATHER)

    await message.answer(city_weather)

if __name__ == '__main__':
    tracemalloc.start()
    executor.start_polling(dp)