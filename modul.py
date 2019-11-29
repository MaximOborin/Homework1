from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
import time
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    logging.info(text)
    update.message.reply_text(text)

def search_planet(bot, update):

    planet = update.message.text.split()[-1]
    now_date = time.strftime('%Y/%m/%d')
    print(planet, now_date)
    if planet == 'Mercury':
        ep_planet = ephem.Mercury(now_date)
    elif planet == 'Venus':
        ep_planet = ephem.Venus(now_date)
    elif planet == 'Mars':
        ep_planet = ephem.Mars (now_date)
    elif planet == 'Jupiter':
        ep_planet = ephem.Jupiter (now_date)
    elif planet == 'Saturn':
        ep_planet = ephem.Saturn(now_date)
    elif planet == 'Uranus':
        ep_planet = ephem.Uranus(now_date)
    elif planet == 'Neptune':
        ep_planet = ephem.Neptune(now_date)
    else:
        print('Ввод неверный')
    const = ephem.constellation(ep_planet)
    print(const)
    user_text_const = f'Планета {planet} сегодня находится в созвездии {const}'
    print(user_text_const)
    update.message.reply_text(user_text_const)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("1038450751:AAGhpHSE0iAXJVTnq1VA26BHZ6nE1P7B2Kg", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', search_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

main()