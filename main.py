import telebot

token = "696340153:AAGCXEzoFj4Ag-f0FPeS-vV-yuHP9rJSQWg"

bot = telebot.TeleBot(token)

message_now = "2-31"

@bot.message_handler(commands=['who_made_this_shit'])
def handle_text(message):
    bot.send_message(message.chat.id, "@tabunshchyk")

@bot.message_handler(commands=['print'])
def handle_text(message):
    bot.send_message(message.chat.id, "2-31")

@bot.message_handler(commands=['price'])
def handle_text(message):
    bot.send_message(message.chat.id, """Текст - 1 грн
Графики ч\б - 1 грн
Графики в цвете - 2 грн
Фото на глянцевой бумаге - 10 грн
Фото на обычной бумаге - 4 грн
Ч\б офто - 3 грн""")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "кто печатает?" or message.text == "кто может напечатать?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "кто-то печатает?" or message.text == "кто может распечатать?":
        bot.send_message(message.chat.id, message_now)
    elif message.text == "кто-то может распечатать?" or message.text == "кто-то может наспечатать?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто печатает?" or message.text == "Кто может напечатать?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто-то печатает?" or message.text == "Кто может распечатать?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто-то может распечатать?" or message.text == "Кто-то может наспечатать?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "кто печатает" or message.text == "кто может напечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "кто-то печатает" or message.text == "кто может распечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "кто-то может распечатать" or message.text == "кто-то может наспечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто печатает" or message.text == "Кто может напечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто-то печатает" or message.text == "Кто может распечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто-то может распечатать" or message.text == "Кто-то может наспечатать" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "У кого есть принтер?" or message.text == "У кого-то есть принтер?" :
        bot.send_message(message.chat.id, message_now)
    elif message.text == "Кто самый пиздатый?" or message.text == "кто самый пиздатый?" :
        bot.send_message(message.chat.id, "@tabunshchyk")
    elif message.text == "Кто-то разрешал добавлять бота?" :
        bot.send_message(message.chat.id, "Меня - да")






bot.polling(none_stop=True, interval=0)

