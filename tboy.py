import telebot
from config import API, TOKEN
import random
import requests
from telebot import types

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row("Search", "Info", " Рандомное число", " Как дeла?", "Планы на завтра")


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('assets/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)


    bot.send_message(message.chat.id,
                     "Ну привет Красавчик".format(message.from_user,
                                                  bot.get_me(

                     )), parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=["search"])
def welcome(message):
    msg = f"<b>Укажите город: </b>"
    bot.send_message(message.chat.id, msg, parse_mode="html")

@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text='Отправить геолокацию', request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, 'Привет, нажми на кнопку отправить геолокацию', reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        print(message.location)
        print('latitude: %s; longitude: %s' %(message.location.longitude, message.location.longitude))    #


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == " Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == " Как дeла?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add (item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?',
                             reply_markup=markup)
        elif message.text == "Search":
            msg = f'<b> "Укажите город:</b>'
            bot.send_message(message.chat.id, msg, parse_mode="html")
        elif message.text == "Info":
            msg = f'''Бот служит для информации и для общения.'''
            bot.send_message(message.chat.id, msg)
        elif message.text == 'Планы на завтра':
            markup=types.InlineKeyboardMarkup(row_width=2)
            item1= types.InlineKeyboardButton('Пойду на курсы', callback_data='go')
            item2= types.InlineKeyboardButton('Останусь дома', callback_data='home')
            markup.add (item1,item2)

            bot.send_message(message.chat.id, 'я вот тебе помогаю',
                            reply_markup=markup)
        else:
            try:
                CITY = message.text
                URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API}'
                response = requests.get(url = URL).json()
                city_info = {
                    "city":CITY,
                    'temp':response['main']['temp'],
                    'weather':response['weather'][0]['description'],
                    'wind':response['wind']['speed'],
                    'pressure':response['main']['pressure'],
                }
                msg = f"<b><u>{CITY.upper()}</u>\n\nWeather is {city_info['weather']}</b>\n----------------------------------\nTemperature: <b>{city_info['temp']} C</b>\n Wind: <b>{city_info['wind']} m/s</b>\n Pressure: <b>{city_info['pressure']}hPa</b>"
                bot.send_message(message.chat.id, msg, parse_mode="html")
            except:
                msg1 = f"<b> Nothing found to country. Try again</b>"
                bot.send_message(message.chat.id, msg1, parse_mode="html")




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает')
            elif call.data == "go":
                bot.send_message(call.message.chat.id, 'Удачи')
            elif call.data == "home":
                bot.send_message(call.message.chat.id, 'Работай')

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Как дела?",
                                  reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text="Это тестовое уведомление")
            

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)