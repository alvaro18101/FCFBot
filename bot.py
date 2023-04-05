import requests
import schedule

def bot_send_text(bot_message):
    bot_token = '6031954984:AAG46zwweNnSGryV57ZeMlzlgDg_z4Gbbj8'
    bot_chatID = '1395536533'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response

# test_bot = bot_send_text('Inicia el bot con el comando /start')


import telebot
from config import *
from functions import *
bot = telebot.TeleBot(token)

# Comando /start
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, welcome)

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.reply_to(message, help)

# Los demás comandos deben ir aquí
# @bot.message_handler(commands=['freeroom'])
# def cmd_freeroom(messsage):
#     bot.reply_to(messsage,df_string)


# ----------------------------------------------------------

@bot.message_handler(content_types=['text', 'sticker'])
def bot_text_message(message):
    bot.send_message(message.chat.id, 'Inicia el bot con el comando /start y si quieres ayuda usa el comando /help')

def cmd_freeroom():
    bot_send_text(rspta1)
if __name__ == '__main__':
    # print('Iniciando el bot')
    schedule.every().day.at("02:52").do(cmd_freeroom)
    # bot.infinity_polling()
    while True:
        schedule.run_pending()
    # print('Finalizado')