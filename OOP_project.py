import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CurencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
      greet= 'Greetings! To get started, enter a command in the format: \n Currency to convert,'\
 'Currency to which needfull converted,'\
 'Converted currency amount\n \n Check all availible currencies: /values'
      bot.reply_to(message, greet)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(',')
    try:
        if len(values) != 3:
            raise ConvertionException('Invalid number of parameters, enter the three parameters: \n converted curency,currency to which needfull converted,converted currency amount')

        quote, base, amount = values
        total_base = CurencyConverter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'User error:\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Request is failed:\n{e}')
    else:
        text = f'The price of {amount} {quote} in {base} is {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

