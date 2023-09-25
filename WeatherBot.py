import asyncio
from aiogram import Bot, types, Dispatcher, executor
import tracemalloc
from main_dates import TOKEN_BOT , API_WEATHER
from GetWeather import get_weather


bot = Bot(token=TOKEN_BOT) 
dp = Dispatcher(bot) 

@dp.message_handler(commands=['start'])
async def start_bot (message: types.Message):
    await message.answer('Если хотите получить самую свежую информацию по погоде, то пишите название города , а остальное я сделаю все сам')

@dp.message_handler()
async def weather_city(message: types.Message):
    dates, check = get_weather(message.text, API_WEATHER)

    await message.answer(dates)

if __name__ == '__main__':
    tracemalloc.start()
    executor.start_polling(dp)