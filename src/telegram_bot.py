"""
Module representing telegram bot
"""
import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# if this exception raised then a programmer forgot to expotr his token which means that program can't contuinue working
if BOT_TOKEN is  None:
    raise Exception

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    Sends welcome message to an user
    """
    bot.reply_to(message, "Hellow, welcome to flightsIO, use /help to see my functionalities")

@bot.message_handler(commands=['help'])
def show_functionalities(message):
    """
    Shows all functionalities that bot has
    """
    bot.reply_to(message, "For now I have only one functionality:")
    text = "Use */cheapest_flights* to get up to 100 avaliable flights"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
