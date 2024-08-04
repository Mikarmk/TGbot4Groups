import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 'There should be a token here'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Доброе)")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_member = update.message.new_chat_members[0]
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=f"Добро пожаловать, {new_member.mention_html()}! Рад видеть тебя в нашей группе!", parse_mode='HTML')

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    app.run_polling()

if __name__ == '__main__':
    main()
