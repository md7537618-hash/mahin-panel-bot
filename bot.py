from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8812803897:AAGRojAYEy3-cZaZPFQvozGozp7H0WlNaTU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Reply Panel", callback_data="reply")],
        [InlineKeyboardButton("🔥 BR Mods Root Panel", callback_data="brmods")],
        [InlineKeyboardButton("⚡ Prime Hook Panel", callback_data="prime")],
        [InlineKeyboardButton("💎 Diamond Seller", callback_data="diamond")],
        [InlineKeyboardButton("📲 All Panel APK", url="https://t.me/+rE6MPCMPs1A1MDdl")],
        [InlineKeyboardButton("👤 Mahin Vai", url="https://t.me/Hacar49MahinVai")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌸 Welcome To Mahin Vai Panel Store 🌸\n\nনিচের বাটন থেকে আপনার পছন্দের অপশন নির্বাচন করুন।",
        reply_markup=reply_markup
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling(drop_pending_updates=True)
