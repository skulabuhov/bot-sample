from telegram import Update
from telegram.ext import CallbackContext


async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Я Вас понял 😎")
