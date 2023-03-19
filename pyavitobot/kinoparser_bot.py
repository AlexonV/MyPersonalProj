"""
"""

import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs
import telebot as tb
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = input()
bot = tb.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup()
    but1, but2 = KeyboardButton('Найти фильм'),KeyboardButton('Найти сериал')
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,'Что вы хотите сделать?',reply_markup= markup)

bot.infinity_polling()
