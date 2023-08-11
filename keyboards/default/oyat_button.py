import requests
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Oyatlar')]],resize_keyboard=True)

def oyat_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json'
    respons = requests.get(url=url).json()
    oyatlar = respons["chapters"]
    for i in oyatlar:
        markup.insert(KeyboardButton(text=f'{i["chapter"]}.{i["name"]}'))
    return markup

back_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="⬅️Orqaga")]],resize_keyboard=True)