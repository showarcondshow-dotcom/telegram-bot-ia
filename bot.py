import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")  # Pega o token do Render

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Eu sou seu bot no Telegram 🤖")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))

print("Bot iniciado...")
updater.start_polling()
updater.idle()
