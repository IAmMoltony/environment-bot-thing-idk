#!/usr/bin/python3

import telebot
import task
import random

# fetch token from ./token.txt so that i don't have to hard-code it
token = ""
with open("./token.txt", "r") as token_file:
    token = token_file.read().strip()

bot = telebot.TeleBot(token)

tasks = task.load_tasks()

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.reply_to(message, 'Hello, this is env-bot. Please use the /help command to get a list of commands')

@bot.message_handler(commands=['help'])
def command_help(message):
    bot.reply_to(message, '`/help` \\- show this help\n`/task [difficulty]` \\- suggest a task with an optional difficulty\\. Valid difficulties are `easy`, `normal` and `hard`\\. Not specifying a difficulty will suggest a task of any difficulty\\.', parse_mode='MarkdownV2')

@bot.message_handler(commands=['task'])
def command_task(message):
    args = message.text.split()
    if len(args) >= 2:
        # this means there is an argument (difficulty)
        # but remember, we never trust user input, so check if it's an actual difficulty first
        user_difficulty = args[1]
        if task.is_valid_difficulty(user_difficulty):
            filtered_tasks = [task for task in tasks if task.difficulty == user_difficulty]
            bot.reply_to(message, str(random.choice(filtered_tasks)), parse_mode='MarkdownV2')
        else:
            bot.reply_to(message, str(random.choice(tasks)), parse_mode='MarkdownV2')
    else:
        bot.reply_to(message, str(random.choice(tasks)), parse_mode='MarkdownV2')

bot.polling()
