import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Vamos criar no Render

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# ---- Comandos ----
async def start(update: Update, context):
    await update.message.reply_text("Olá! Eu sou seu bot no Telegram 🤖")

application.add_handler(CommandHandler("start", start))

# ---- Webhook endpoint ----
@app.post("/")
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "OK", 200

# ---- Inicialização ----
if __name__ == "__main__":
    # Ativa webhook quando iniciar
    application.bot.set_webhook(url=os.getenv("WEBHOOK_URL"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

