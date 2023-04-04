import requests

def bot_send_text(bot_message):
    bot_token = '6031954984:AAG46zwweNnSGryV57ZeMlzlgDg_z4Gbbj8'
    bot_chatID = '1395536533'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response

# test_bot = bot_send_text('Inicia el bot con el comando /start')


import telebot
from config import *
bot = telebot.TeleBot(token)

# Comando /start
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, 'Bienvenido estudiante de la FCF')

@bot.message_handler(content_types=['text', 'sticker'])
def bot_text_message(message):
    bot.send_message(message.chat.id, 'Inicia el bot con el comando /start y si quieres ayuda usa el comando /help')


if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Finalizado')
