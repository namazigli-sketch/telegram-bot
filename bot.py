import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من ربات تلگرام گلبهار هستم. خوش آمدی!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable not set.")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
