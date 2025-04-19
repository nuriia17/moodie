import logging
import json
import random
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка цитат
DATA_FILE = Path("data/quotes.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    quotes = json.load(f)

# Настроения (ключи json)
MOODS = ["motivation", "sad", "angry", "happy", "hungry"]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💪 Motivation", callback_data='motivation')],
        [InlineKeyboardButton("😢 Sad", callback_data='sad')],
        [InlineKeyboardButton("😡 Angry", callback_data='angry')],
        [InlineKeyboardButton("😊 Happy", callback_data='happy')],
        [InlineKeyboardButton("🍔 Hungry", callback_data='hungry')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose your mood:", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    mood = query.data

    await query.answer()
    if mood in quotes:
        text = random.choice(quotes[mood])
        await query.edit_message_text(text=text)
    else:
        await query.edit_message_text(text="No quotes available for this mood.")

# Основной запуск
def main():
    # 🔑 ЗАМЕНИ НА СВОЙ ТОКЕН
    TOKEN = "7776922220:AAFee3gYvklptkSJi1BoRa4OGxSs_AfMapg"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_mood))

    logger.info("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
