#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import NetworkError, Unauthorized
from time import sleep

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Vamos começar, bicha!')


def oi(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Oi Matheus Viadão!')

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Run the bot."""
    # Telegram Bot Authorization Token
    updater = Updater("544501699:AAG3vYB04v6aNK5Qxy2jsmATpoqDinEaf2s")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("oi", oi))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()