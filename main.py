import telebot

bot = telebot.TeleBot("6464592977:AAEIyyp4KiHJ8S-OBuG-dX2aGTZENzRntTM")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Приветствую тебя, мой дорогой и отважный герой")


@bot.message_handler(commands=["joke"])
def joke_handler(message):
    bot.send_message(message.chat.id,
                     "-Назовите свои сильные стороны.\n-Настойчивость.\n-Спасибо, мы с вами свяжемся.\n-Я подожду здесь.")


@bot.message_handler(commands=["weather"])
def weather_handler(message):
    bot.send_message(message.chat.id,
                     "[**Погода на ближайшие десять дней в нашем лесу**](https://www.gismeteo.ru/weather-moscow-4368/10-days/)")


@bot.message_handler(commands=["mystery"])
def mystery_handler(message):
    bot.send_message(message.chat.id, "_Что не вместиться даже в самую большую кастрюлю?_")


@bot.message_handler(commands=["survey"])
def survey_handler(message):
    bot.send_message(message.chat.id,
                     "Здорово, что ты готов пройти опрос, путник.Тогда начнем с чего-нибудь полегче.Например, сколько ног у многоножки?")


bot.infinity_polling()