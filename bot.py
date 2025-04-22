from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

FLAG = "Honoured to deliver you the flag master - 'Hedwig'"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FLAG)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Respond to any text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
