"""
Module representing telegram bot
"""
import os
import telebot
from utils import get_tickets,is_valid_date, is_valid_city

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
    text = "Input *IATA* (3 cahracter long) code of the departure city"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, to_handler)


def to_handler(message):
    """
    Requests destination city
    """
    city_from = message.text
    if not is_valid_city(city_from.upper()):
        bot.send_message(message.chat.id, "Invalid *IATA* code of a departure city.", parse_mode="Markdown")
        sent_msg = bot.send_message(message.chat.id, "Input *IATA* (3 cahracter long) code of the departure city", parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,to_handler)
        return

    text = "Input *IATA* (3 cahracter long) code of the destination city\nfor all routes, enter *\"-\"*"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,departure_date_handler, city_from.upper())

def departure_date_handler(message,city_from):
    """
    Requests deaprture date
    """
    city_to = message.text
    if not is_valid_city(city_to.upper()) and not city_to == '-':
        bot.send_message(message.chat.id, "Invalid *IATA* code of a destination city.", parse_mode="Markdown")
        sent_msg = bot.send_message(message.chat.id, "Input *IATA* (3 cahracter long) code of the destination city\nfor all routes, enter *\"-\"*", parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,departure_date_handler, city_from)
        return

    text = "Input departure date/month in *YYYY-MM-DD / YYYY-MM* format\nfor not specified departure date, enter *\"-\"*"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,return_date_handler, city_from, city_to.upper())

def return_date_handler(message,city_from,city_to):
    """
    Requests return date
    """
    departure_date = message.text
    text = "Input return date/month in *YYYY-MM-DD / YYYY-MM* format\nfor not specified return date, enter *\"-\"*"
    
    if not is_valid_date(departure_date) and not departure_date == "-":
        bot.send_message(message.chat.id, "Incorrect date format, should be *YYYY-MM-DD*", parse_mode="Markdown")
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,return_date_handler, city_from, city_to)
        return

    if departure_date == "-":
        departure_date = ""

    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, currency_handler, city_to, city_from, departure_date)

# i think i will remove a possibility for diff currencies
def currency_handler(message,city_from,city_to, departure_date):
    """
    Requests currency
    """
    return_date = message.text
    text = "Input currency\nfor default currency (EUR), enter *\"-\"* "
    
    if not is_valid_date(return_date) and not return_date == "-":
        bot.send_message(message.chat.id, "Incorrect date format, should be *YYYY-MM-DD*", parse_mode="Markdown")
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,currency_handler, city_from, city_to,departure_date)
        return
    
    if return_date == "-":
        return_date = ""
    
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
    tickets = get_tickets(departure_date, return_date,city_from,city_to,currency )
    #TODO: add page feature to show more that 4096 symbols aka mulyiple responses
    # is it okay error handling?
    if tickets is None:
        bot.send_message(message.chat.id, "We appologise, an error accuried while searching, please try again later.")
        return

    if tickets:
        #builds a list of tickets with length <= max possible output
        max_result = [x for index, x in enumerate(tickets) if index < MAX_LENGTH_OF_OUTPUT and x is not None]
        text = "".join([ str(ticket) + "\n" for ticket in max_result])
        bot.send_message(message.chat.id, "Here are your cheapest tickets!")
        bot.send_message(message.chat.id, text)
        return

    bot.send_message(message.chat.id, "No flights were found within given information.")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
