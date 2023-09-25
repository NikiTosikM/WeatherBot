from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

user_cities = {}

def keyboard_buttons(city, check):
    
    keyboard_bot = ReplyKeyboardMarkup()

    if check:
        if city in user_cities:
            user_cities[city] += 1
        else:
            user_cities[city] = 1

        sorted_cities = [name[0] for name in sorted(user_cities.items(), key= lambda x: x[1], reverse=True)]
        keyboard_bot = ReplyKeyboardMarkup()

        for city in sorted_cities[:3]:
            button = KeyboardButton(city)
            keyboard_bot.add(button)

        return keyboard_bot

    else:
        return keyboard_bot