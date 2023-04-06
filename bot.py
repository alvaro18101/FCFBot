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
@bot.message_handler(commands=['list'])
def cmd_help(message):
    bot.reply_to(message, str(lista_aulas))


@bot.message_handler(commands=['freeroom'])
def cmd_freeroom(messsage):
    # Código para obtener la fecha y hora del momento en que se ingresa el comando
    today = days[datetime.today().weekday()]
    hour = datetime.today().hour
    minutes = datetime.today().minute
    # Código para seleccionar las aulas que están libres ese día --> devuelve una lista
    
    bot.reply_to(messsage,'Consulta realizada el {} a las {}:{}\n' .format(today,hour,minutes) + freeroom_text)


# ----------------------------------------------------------
@bot.message_handler(content_types=['text', 'sticker'])
def bot_text_message(message):
    bot.send_message(message.chat.id, 'Inicia el bot con el comando /start y si quieres ayuda usa el comando /help')

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Finalizado')

    # schedule.every().day.at("12:52").do(cmd_freeroom)
    # while True:
    #     schedule.run_pending()