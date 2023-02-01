"""
Module representing telegram bot
"""
import os
import telebot
from utils import get_tickets

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

@bot.message_handler(commands=['cheapest_flights'])
def from_handler(message):
    """
    Requests departure city
    """
    text = "Input *IATA* (2 or 3 cahracter long) code of the departure city"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, to_handler)


def to_handler(message):
    """
    Requests destination city
    """
    city_from = message.text
    # validate city_form
    text = "Input *IATA* (2 or 3 cahracter long) code of the destination city\nfor all routes, enter *-*"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,departure_date_handler, city_from.upper())

def departure_date_handler(message,city_from):
    """
    Requests deaprture date
    """
    city_to = message.text
    # validate city_to
    text = "Input departure date/month in *YYYY-MM-DD / YYYY-MM* format\nfor not specified departure date, enter *-*"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,return_date_handler, city_from, city_to.upper())

def return_date_handler(message,city_from,city_to):
    """
    Requests return date
    """
    departure_date = message.text
    # validate departure_date && checks if is '-'
    text = "Input return date/month in *YYYY-MM-DD / YYYY-MM* format\nfor not specified return date, enter *-*"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, currency_handler, city_to, city_from, departure_date)

# i think i will remove a possibility for diff currencies
def currency_handler(message,city_from,city_to, departure_date):
    """
    Requests currency
    """
    return_date = message.text
    # validate return_date && checks if is '-'
    text = "Input currency\nfor default currency (EUR), enter *-* "
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, find_tickets, city_to, city_from, departure_date, return_date)

# the 2 is for new line in response ('\n')
TICKET_LENGTH = 82+ 2
MAX_RESPONSE_SIZE = 4096
MAX_LENGTH_OF_OUTPUT = MAX_RESPONSE_SIZE // TICKET_LENGTH
def find_tickets(message,city_from,city_to, departure_date, return_date):
    """
    Returns tickets
    """
    currency = message.text
    # validate currency? && checks if is '-'
    tickets = get_tickets(departure_date, return_date,city_from,city_to,currency )
    # convert into list comp
    # check if any results in range

    #builds a list of tickets with length <= max possible output
    #TODO: add page feature to show more that 4096 symbols aka mulyiple responses
    max_result = [x for index, x in enumerate(tickets) if index < MAX_LENGTH_OF_OUTPUT and x is not None]
    text = "".join([ str(ticket) + "\n" for ticket in max_result])
    bot.send_message(message.chat.id, "Here are your cheapest tickets!\n")
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
