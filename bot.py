# -*- coding: utf-8 -*-

import telebot
import json

TOKEN = ""


with open("vacancies.json", "r") as read_file:
    data = json.load(read_file)

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я покажу тебе все вакасии.")
      bot.send_message(message.from_user.id, json.dumps(data))

  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)