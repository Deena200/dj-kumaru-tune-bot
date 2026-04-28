import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

async def mass_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    await update.message.reply_text(
        f"🔥 Mass BGM requested by {user}\n\nChecking voice chat..."
    )

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "DJ Kumaru Music Bot is live 🎧"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("mass", mass_command))

print("🔥 DJ Kumaru Music Bot Running...")
app.run_polling()
