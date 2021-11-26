import telebot
import requests
import json
import random
#from pytube import YouTube
from telebot import types

# Google Cloud Translate API
api = 'AIzaSyB5xVmGc6pjl-7BqUbKZDvRDA_F02X9yLE'

# Telegram Bot token
token = '2101285616:AAEjFs9SBbuw5ikyW0l3qUPJrNR0BYqbH7w'
bot = telebot.TeleBot(token)
url = 'https://translation.googleapis.com/language/translate/v2'
# Create a list of random kazakh names
names = ["Arman", "Erzhan", "Erkezhan", "Azamat", "Bekbolat", "Alua","Aydana","Zhansaya","Aysana","Shynar","Aslan","Fatima","Narikbi"]

# Create a list of random fairy tales
tales_kazakh = [
    "Kіshkentaı aqyldy balapan \n https://www.youtube.com/watch?v=oXvarJiN-YU",
    "USh TORAI OQIGASY \n https://www.youtube.com/watch?v=iLpeMvCLHgg&list=PL_zebziuroEd3aP5I23CD_QGRVC_TI1kZ",
    "Qoshqar men teke \n https://www.youtube.com/watch?v=pGrzpCoJGGI",
    "Jaqsylyq pen jamandyq \n https://www.youtube.com/watch?v=Yi-0x98XJXg ",
    "Qadіrdіń baqyty \n https://www.youtube.com/watch?v=VGsVuWROs6g "
]

tales_kyrgyz = [
    "Kіshkentaı aqyldy balapan \n https://www.youtube.com/watch?v=oXvarJiN-YU",
    "USh TORAI OQIGASY \n https://www.youtube.com/watch?v=iLpeMvCLHgg&list=PL_zebziuroEd3aP5I23CD_QGRVC_TI1kZ",
    "Qoshqar men teke \n https://www.youtube.com/watch?v=pGrzpCoJGGI",
    "Jaqsylyq pen jamandyq \n https://www.youtube.com/watch?v=Yi-0x98XJXg ",
    "Qadіrdіń baqyty \n https://www.youtube.com/watch?v=VGsVuWROs6g "
]
tales_russian = [
    "Kіshkentaı aqyldy balapan \n https://www.youtube.com/watch?v=oXvarJiN-YU",
    "USh TORAI OQIGASY \n https://www.youtube.com/watch?v=iLpeMvCLHgg&list=PL_zebziuroEd3aP5I23CD_QGRVC_TI1kZ",
    "Qoshqar men teke \n https://www.youtube.com/watch?v=pGrzpCoJGGI",
    "Jaqsylyq pen jamandyq \n https://www.youtube.com/watch?v=Yi-0x98XJXg ",
    "Qadіrdіń baqyty \n https://www.youtube.com/watch?v=VGsVuWROs6g "
]
tales_english = [
    "Kіshkentaı aqyldy balapan \n https://www.youtube.com/watch?v=oXvarJiN-YU",

    "USh TORAI OQIGASY \n https://www.youtube.com/watch?v=iLpeMvCLHgg&list=PL_zebziuroEd3aP5I23CD_QGRVC_TI1kZ",
    "Qoshqar men teke \n https://www.youtube.com/watch?v=pGrzpCoJGGI",
    "Jaqsylyq pen jamandyq \n https://www.youtube.com/watch?v=Yi-0x98XJXg ",
    "Qadіrdіń baqyty \n https://www.youtube.com/watch?v=VGsVuWROs6g "
]

songs_1 = [
    "https://www.youtube.com/watch?v=EoRbSLtPN4k",
    "https://www.youtube.com/watch?v=kZflInXzJ2w",
    "https://www.youtube.com/watch?v=ojfn8ivjNoo"
]
songs_2 = [
    "https://www.youtube.com/watch?v=eZzOkjGPR_Y",
    "https://www.youtube.com/watch?v=P-F88_oGn30",
    "https://www.youtube.com/watch?v=YPufRvMNw14"
]
# Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello, {0.first_name}!\n Я, очень добрая - <b>{1.first_name}</b>. Умею переводить на казахский и конвертировать с кириллицы на латиницу. Могу посоветовать имя для немере, найти сказки, песни на казахском или же рассказать про великих людей. В общем бабушкан 24/7 тигр гой \n Если хочешь перевести слова напиши мне как сообщение, а если хочешь попробовать другие фишки используй команду /help ".format(message.from_user, bot.get_me()),
                    parse_mode='html')
@bot.message_handler(commands=['help'])
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Create two buttons
    item1 = types.KeyboardButton("Random kazakh name")
    item2 = types.KeyboardButton("Fairy tales")
    item3 = types.KeyboardButton("Music")
    item4= types.KeyboardButton("Great people")
    item5=types.KeyboardButton("Museum")
    markup.add(item1, item2,item3, item4,item5)
    bot.send_message(message.chat.id, "слушаю, что хочешь узнать ",
        parse_mode='html', reply_markup=markup)


# Get response
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    # message.text text of client
    usertext = message.text
    if message.text == 'Random kazakh name':
        # randomly get name from array
        bot.send_message(message.chat.id, random.choice(names))
    # elif message.text == 'Fairy tales':
    #     # show buttons to choose language


    #         markup=types.InlineKeyboardMarkup(row_width=4)
    #         item1= types.InlineKeyboardButton('Russian fairy tales', callback_data='Russian fairy tales')
    #         item2= types.InlineKeyboardButton('Kyrgyz fairy tales', callback_data='Kyrgyz fairy tales')
    #         item3= types.InlineKeyboardButton('English fairy tales', callback_data='English fairy tales')
    #         item4= types.InlineKeyboardButton('Kazakh fairy tales', callback_data='Kazakh fairy tales')
    #         markup.add (item1,item2,item3,item4)

    #         bot.send_message(message.chat.id, 'Choose language',
    #                         reply_markup=markup)

    elif message.text == 'Fairy tales':
            markup=types.InlineKeyboardMarkup(row_width=4)
            item1= types.InlineKeyboardButton('Russian', callback_data='Russian')
            item2= types.InlineKeyboardButton('Kyrgyz', callback_data='Kyrgyz')
            item3= types.InlineKeyboardButton('English', callback_data='English')
            item4= types.InlineKeyboardButton('Kazakh', callback_data='Kazakh')
            markup.add (item1,item2,item3,item4)
            bot.send_message(message.chat.id, 'Choose language of the fairytale', reply_markup=markup)   


    # elif message.text == 'Fairy tales':
    #     # randomly get fairy tale from array
    #     bot.send_message(message.chat.id, random.choice(tales_kazakh))
    # elif message.text == 'Fairy tales':
    #     # randomly get fairy tale from array
    #     bot.send_message(message.chat.id, random.choice(tales_kyrgyz))
    # elif message.text == 'Fairy tales':
    #     # randomly get fairy tale from array
    #     bot.send_message(message.chat.id, random.choice(tales_russian))
    # elif message.text == 'Fairy tales':
    #     # randomly get fairy tale from array
    #     bot.send_message(message.chat.id, random.choice(tales_english))

    # #need to correct to choose to code for user
    #         elif message.text == " Как дeла?":

    #         markup = types.InlineKeyboardMarkup(row_width=2)
    #         item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
    #         item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

    #         markup.add (item1, item2)

    #         bot.send_message(message.chat.id, 'Отлично, сам как?',
    #                          reply_markup=markup)

        # elif message.text == 'Планы на завтра':
        #     markup=types.InlineKeyboardMarkup(row_width=2)
        #     item1= types.InlineKeyboardButton('Пойду на курсы', callback_data='go')
        #     item2= types.InlineKeyboardButton('Останусь дома', callback_data='home')
        #     markup.add (item1,item2)

        #     bot.send_message(message.chat.id, 'я вот тебе помогаю',
        #                     reply_markup=markup)







    elif message.text == 'Music':
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        item11 = types.InlineKeyboardButton("Kúı", callback_data='Kúı')
        item22 = types.InlineKeyboardButton("Án", callback_data='Án')
        markup1.add(item11, item22)
        bot.send_message(message.chat.id, 'Что хочешь послушать', reply_markup=markup1)
    elif message.text == 'Great people':
        markup2 = types.InlineKeyboardMarkup(row_width=2)
        item12 = types.InlineKeyboardButton("Abai", callback_data='p1')
        item221 = types.InlineKeyboardButton("Shoqan", callback_data='p2')
        item222 = types.InlineKeyboardButton("Ybyraı", callback_data='p3')
        markup2.add(item12, item221,item222)
        bot.send_message(message.chat.id, 'Что хочешь послушать', reply_markup=markup2)
    elif message.text=="Museum":
        mus_lat,mus_lon=43.2355665, 76.9487616
        bot.send_location(message.chat.id,mus_lat,mus_lon)
        bot.send_message(message.chat.id, '44, мк-он Самал-1, д, Алматы')
    else:
        # Prepare object for the request
        myObj = {'key': api, 'q': usertext, 'target': 'kk', 'format': 'text'}
        
        # Send a request to Cloud Translate API
        x = requests.post(url, data=myObj)

        # Get response as a translated text
        response = json.loads(x.text)["data"]["translations"][0]["translatedText"]

        # Convert the letter by method replace
        final = response.replace("я", "ıa").replace("э", "e").replace("Э", "E").replace("Я", "Ia").replace("ю",
                                                                                                        "ıý").replace(
            "Ю", "Iý").replace("ц",
                            "ts").replace(
            "а", "a").replace("ә", "á").replace("б", "b").replace("д", "d").replace("е",
                                                                                    "e").replace(
            "ф", "f").replace("г", "g").replace("ғ", "ǵ").replace("х", "h").replace("һ", "h").replace("і",
                                                                                                    "i").replace(
            "и", "ı").replace("й", "ı").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м",
                                                                                                    "m").replace(
            "н", "n").replace("ң", "ń").replace("о", "o").replace("ө", "ó").replace("п", "p").replace("қ",
                                                                                                    "q").replace(
            "р", "r").replace("с", "s").replace("ш", "sh").replace("щ", "sh").replace("ч", "ch").replace("т",
                                                                                                        "t").replace(
            "ұ", "u").replace("ү", "ú").replace("в", "v").replace("ы", "y").replace("у", "ý").replace("з",
                                                                                                    "z").replace(
            "ь", "").replace("ъ", "").replace("Ъ", "").replace("Ь", "").replace("А", "A").replace("Ә", "Á").replace(
            "Б",
            "B").replace(
            "Д",
            "D").replace(
            "Е", "E").replace("Ф", "F").replace("Г", "G").replace("Ғ", "Ǵ").replace("Х", "H").replace("І",
                                                                                                    "I").replace(
            "Й", "I").replace("И", "I").replace("Ж", "J").replace("К", "K").replace("Л", "L").replace("М",
                                                                                                    "M").replace(
            "Н", "N").replace("Ң", "Ń").replace("О", "O").replace("Ө", "Ó").replace("П", "P").replace("Қ",
                                                                                                    "Q").replace(
            "Р", "R").replace("С", "S").replace("Ш", "Sh").replace("Щ", "Sh").replace("Ч", "Ch").replace("Т",
                                                                                                        "T").replace(
            "Ұ", "U").replace("Ү", "Ú").replace("В", "V").replace("Ы", "Y").replace("У", "Ý").replace("З",
                                                                                                    "Z").replace(
            "ё", "е").replace("Ё", "E")
        
        # Finally sending result message
        bot.send_message(message.chat.id, final)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
            if call.message:  # true
                if call.data == 'Kúı':
                    bot.send_message(call.message.chat.id, random.choice(songs_1))
                elif call.data == 'Án':
                    bot.send_message(call.message.chat.id, random.choice(songs_2))

                if call.data == 'Russian':
                    bot.send_message(call.message.chat.id, random.choice(tales_russian))
                elif call.data == 'Kyrgyz':
                    bot.send_message(call.message.chat.id, random.choice(tales_kyrgyz))

                if call.data == 'English':
                    bot.send_message(call.message.chat.id, random.choice(tales_english))
                elif call.data == 'Kazakh':
                    bot.send_message(call.message.chat.id, random.choice(tales_kazakh))
                elif call.data=='p1':
                    p1=open("p1.jpg",'rb')
                    bot.send_photo(call.message.chat.id, p1)
                    p1_a=open('one.ogg','rb')
                    bot.send_message(call.message.chat.id, 'Аудио было сделанно благодаря боту @kzttsbot  демонстрирующий возможности сервиса по синтезу речи на казахском языке.Дружеский PR')
                    bot.send_audio(call.message.chat.id, p1_a)
                elif call.data=='p2':
                    p2=open('p2.jpg','rb' )
                    bot.send_photo(call.message.chat.id, p2)
                    p2_a = open('th.ogg', 'rb')
                    bot.send_audio(call.message.chat.id, p2_a)
                    bot.send_message(call.message.chat.id,'Аудио было сделанно благодаря боту @kzttsbot  демонстрирующий возможности сервиса по синтезу речи на казахском языке.Дружеский PR')
                elif call.data=='p3':
                    p3=open('p3.jpg','rb')
                    bot.send_photo(call.message.chat.id, p3)
                    p3_a = open('two.ogg', 'rb')
                    bot.send_audio(call.message.chat.id, p3_a)
                    bot.send_message(call.message.chat.id,'Аудио было сделанно благодаря боту @kzttsbot  демонстрирующий возможности сервиса по синтезу речи на казахском языке.Дружеский PR')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Hope you like it', reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Demal')

#code in order to choose the language for user
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'Russian':
#                 # randomly get fairy tale from array
#                 bot.send_message(message.chat.id, random.choice(tales_russian))
#             elif call.data == 'Kyrgyz':
#                 # randomly get fairy tale from array
#                 bot.send_message(message.chat.id, random.choice(tales_kyrgyz))
#             elif call.data == "English":
#                 # randomly get fairy tale from array
#                 bot.send_message(message.chat.id, random.choice(tales_english))
#             elif call.data == "Kazakh":
#                 # randomly get fairy tale from array
#                 bot.send_message(message.chat.id, random.choice(tales_kazakh))

#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.message_id,
#                                   text="Fairy tales",
#                                   reply_markup=None)

#             bot.answer_callback_query(callback_query_id=call.id,
#                                       show_alert=False,
#                                       text="Это тестовое уведомление")


            # item1= types.InlineKeyboardButton('Russian fairy tales', callback_data='Russian fairy tales')
            # item2= types.InlineKeyboardButton('Kyrgyz fairy tales', callback_data='Kyrgyz fairy tales')
            # item3= types.InlineKeyboardButton('English fairy tales', callback_data='English fairy tales')
            # item4= types.InlineKeyboardButton('Kazakh fairy tales', callback_data='Kazakh fairy tales')




    # elif message.text == 'Fairy tales':
    #     # randomly get fairy tale from array
    #     bot.send_message(message.chat.id, random.choice(tales_kazakh))



# if __name__ == '__main__':
#     bot.polling(none_stop=True)


    # except Exception as e:
    #     print(repr(e))

bot.polling(none_stop=True)






#bektur send message
# import telebot
# from telebot.types import Message
# from telebot import types
# from pytube import YouTube
# import os

# # initialization

# api = ' ' # api key from telegram @BotFather
# bot = telebot.TeleBot(api)

# link = []

# # emojis
# audio_emoji = u'\U0001F3B5'
# video_emoji = u'\U0001F3AC'
# error_emoji = u'\U00002716'
# download_emoji = u'\U00002B07'
# done_emoji = u'\U00002714'


# @bot.message_handler(commands=['start']) # Welcome message
# def send_welcome(message):
#     bot.reply_to(message, "To download audio or video from YouTube or YouTube Music send me a link.")


# @bot.message_handler(content_types=['text'])
# def url_handler(message):
#     text = message.text # Checking the link
#     if 'https://www.youtube.com/' in text or 'https://youtube.com/' in text \
#             or 'https://music.youtube.com/' in text or 'https://youtu.be/' in text \
#             or 'https://m.youtube.com/' in text: 
#         link.append(text)
#         save_buttons(message)
#     else:
#         bot.send_message(message.chat.id, 'Please, send me a YouTube link.')


# def save_buttons(message): # Buttons added for user choices
#     keyboard = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton(text='Audio' + audio_emoji, callback_data='save_audio')
#     button2 = types.InlineKeyboardButton(text='Video' + video_emoji, callback_data='save_video')
#     keyboard.add(button1, button2)
#     bot.send_message(message.chat.id, 'What do you want to download?', reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call: True)
# def buttons(call):
#     if call.data == 'save_audio':
#         save_audio(call.message)

#     elif call.data == 'save_video':
#         save_video(call.message)


# def save_audio(message):
#     try:
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Audio download has started.' + download_emoji)
#         url = link # link = message text
#         yt = YouTube(str(url))
#         ys = yt.streams.get_audio_only()
#         audio = ys.download() # audio download
#         name = yt.title # saving video title to rename the file
#         os.rename(audio, 'audio.mp3') # file renaming for correct deletion

#         audio = open('audio.mp3', 'rb')
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Download completed successfully.' + done_emoji)
#         bot.send_audio(message.chat.id, audio, title=name)
#         audio.close()
#         os.remove('audio.mp3') # removing file from the server
#         link.clear() # link clearing for the next url
#     except:
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Failed to upload audio.' + error_emoji)
#         link.clear()


# def save_video(message):
#     try:
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Video download has started.' + download_emoji)
#         url = link # link = message text
#         yt = YouTube(str(url))
#         ys = yt.streams.get_highest_resolution()
#         video = ys.download() # video download
#         os.rename(video, 'video.mp4') # file renaming for correct deletion

#         video = open('video.mp4', 'rb')
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Download completed successfully.' + done_emoji)
#         bot.send_video(message.chat.id, video)
#         video.close()
#         os.remove('video.mp4') # removing file from the server
#         link.clear() # link clearing for the next url

#     except:
#         bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                               text='Failed to upload video.' + error_emoji)
#         link.clear()


# if name == 'main':
#     bot.polling(True)