# Python_Project_FMI
This project was used for final project for Python course in Sofia Univirsity FMI copyng any line of code from this repo could be counted as PLAGIARISM
#Overview
This telegram bot is used to extract information for the cheapest flights based on given trip details. The source of information is the cache from last 2 days of "Aviasales.ru".

# Getting ready
to start using the bot you need to create .env file which contains:
export BOT_TOKEN = [your telegram bot token]
export API_TOKEN = [your API token]

guide how to get your telegram bot token:
  - https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/
to obtain API key you need:
  - register on https://app.travelpayouts.com
  - create a "project"
  - add aviasales module to it
  - request an "API Flight Data Access" token for "money saving"
  
after obtaining token run:
  - source [your filename].env to load tokens into global enviroment.
  
run: "pip install -r requirements.txt"

to start bot itself use: python3 telegram_bot.py 
