import os
import telebot


bot = telebot.TeleBot("5069294704:AAHzRv35QYAzEoXS18qy2qMta2rY-LZyWw4")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm sulochana Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://cybertrackerblog.gq")



bot.polling()