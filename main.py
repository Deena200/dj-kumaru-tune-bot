import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = -1003573621688

music_triggers = ["mass"]

async def music_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower().strip()
        user = update.effective_user.first_name

        if text in music_triggers:
            await update.message.reply_text(
                f"🔥 Mass BGM requested by {user}\n\nChecking voice chat..."
            )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, music_reply)
)

print("🔥 DJ Kumaru Music Bot Running...")
app.run_polling()
