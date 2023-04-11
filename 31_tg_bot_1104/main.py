import telebot
import csv
import random as r

bot = telebot.TeleBot('token')


def update_sticker_collection(emoji, sticker_id):
    with open('stickers.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([emoji, sticker_id])


def get_random_sticker():
    with open('stickers.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        row = r.choice(list(reader))
        return row[0]


@bot.message_handler(commands=['start'])
def start(message):
    msg = 'Привет! Я умею повторять за тобой сообщения!'
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['sticker'])
def send_random_sticker(message):
    stick = get_random_sticker()
    bot.send_sticker(message.chat.id, stick)


@bot.message_handler(content_types=['text'])  # распознавать текст
def echo(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id  # сохраняю id стикера в переменной
    sticker_emoji = message.sticker.emoji  # сохраняю emoji стикера, к которому он привязан
    update_sticker_collection(sticker_id, sticker_emoji)
    bot.reply_to(message, f'ID стикера: {sticker_id}, эмоджи: {sticker_emoji}')


if __name__ == '__main__':  # если запускается именно этот файл, выполнить код условия
    bot.polling()




