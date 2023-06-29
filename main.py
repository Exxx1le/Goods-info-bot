import telebot
from telebot import types

import goods_requests
from api_key import key

bot = telebot.TeleBot(key)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"👋 Привет, {message.from_user.first_name}! Я твой помощник по бьюти-шоппингу."
        f"Чтобы узнать, что я умею, введи /help",
    )


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Я умею проверять информацию о наличии товара в магазине. "
        f"Для этого пришли мне ссылку на интересующий тебя товар 🤓"
        f"Поддерживаемые магазины доступны по запросу /shops",
    )


@bot.message_handler(commands=["shops"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Я умею проверять информацию о наличии товара в "
        f"магазинах {goods_requests.supported_shops}",
    )


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    check = goods_requests.link_checker(message.text)
    if check == "goldapple.ru":
        request_result = goods_requests.gold_apple_stock_status(message.text)
        if request_result is True:
            bot.send_message(
                message.chat.id, f"Товар доступен!!!🤩 Скорее за покупкой!!!🏃‍♀️"
            )
        elif request_result is False:
            bot.send_message(
                message.chat.id, f"Товар отсутствует. Придется еще подождать 🐌"
            )
        else:
            "Проверьте ссылку на товар 🤷‍♂️"
    elif check is False:
        bot.send_message(
            message.chat.id,
            f"К сожалению, такой магазин не поддерживается мной или ссылка некорректна 😞",
        )
    else:
        bot.send_message(
            message.chat.id, f"К сожалению, вы прислали некорректную ссылку 😐"
        )


if __name__ == "__main__":
    bot.polling(none_stop=True)
