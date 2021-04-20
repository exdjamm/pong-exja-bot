#!/bin/python3.8

from telegram.ext import Updater, CommandHandler, MessageHandler, filters

help_msg = """Bot de pong

Digita qualquer coisa e ele ira responder pong."""

## Callbacks
def command_help(update, context):
    print(update, context.args)
    msg = help_msg
    update.message.reply_text(msg)
    pass

def command_start(update, context):
    print(update, context.args)
    msg = help_msg
    update.message.reply_text(msg)
    pass

def on_message(update, context):
    msg = "pong"
    
    update.message.reply_text(msg)

    pass

## Main 
def main():
    updater = Updater("BOT_TOKEN", use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', command_help))
    dispatcher.add_handler(CommandHandler('start', command_start))
    dispatcher.add_handler(MessageHandler(filters.Filters.update, on_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
