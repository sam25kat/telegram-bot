from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7698457313:AAEM3lQWMZ7jtwFUuXpxNGdNoUuFOHg3iq4"
FLAG = "Honoured to deliver you the flag master - 'BIRBAL'"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FLAG)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Respond to any text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
