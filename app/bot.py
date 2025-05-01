from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from app.config import TELEGRAM_BOT_TOKEN
from app.rag_pipeline import generate_answer

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text

    await update.message.reply_text("🤖 Pensando...")

    try:
        response = generate_answer(user_question)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"❌ Ocurrió un error:\n{e}")

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    app.add_handler(handler)

    print("✅ Bot iniciado y escuchando mensajes...")
    app.run_polling()
