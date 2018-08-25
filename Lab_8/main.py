#coding:utf-8
import telebot, config
from test import Recognize
bot = telebot.TeleBot(config.TOKEN)

def FindNumber(message):
    if len(message.text) == 12:
        with open('countries.txt', 'r') as file:
            for line in file:
                if message.text[:len(line.strip().split(',')[0])] == line.strip().split(',')[0]:
                    bot.send_message(message.chat.id, line.strip().split(',')[1])
                    return
            bot.send_message(message.chat.id, "Даний номер не iснує")
    elif len(message.text) == 10:
        text = message.text[1:]
        with open('cities.txt', 'r') as file:
            for line in file:
                if text[:len(line.strip().split(',')[0])] == line.strip().split(',')[0]:
                    if line.strip().split(',')[2]:
                        bot.send_message(message.chat.id, line.strip().split(',')[1] + ', ' + line.strip().split(',')[2])
                    else: bot.send_message(message.chat.id, line.strip().split(',')[1])
                    return
            bot.send_message(message.chat.id, "Даний номер не iснує")
    elif len(message.text) == 9:
        with open('cities.txt', 'r') as file:
            for line in file:
                if message.text[:len(line.strip().split(',')[0])] == line.strip().split(',')[0]:
                    if line.strip().split(',')[2]:
                        bot.send_message(message.chat.id, line.strip().split(',')[1], ',', line.strip().split(',')[2])
                    else: bot.send_message(message.chat.id, line.strip().split(',')[1])
                    return
            bot.send_message(message.chat.id, "Даний номер не iснує")
    else: bot.send_message(message.chat.id, "Некоректний ввiд")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я Telegram бот - iдентифiкую номери")

@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Просто введiть номер або скиньте фото номера")
    bot.send_message(message.chat.id, "/start - початок використання\n/help - допомога")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    FindNumber(message)

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    message.text = Recognize("image.jpg")
    FindNumber(message)

if __name__ == "__main__":
    bot.polling()