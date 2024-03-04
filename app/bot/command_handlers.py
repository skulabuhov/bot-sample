from telegram import Update
from telegram.ext import CallbackContext

GREETING = """Добро пожаловать{greeting_name}!

Этот бот умеет вот это и вот это

Для получения того-то выполните команду:
/togo_to

Для аолучения вот этого выполните команду:
/vot_eto

Желаем Вам удачи!"""


async def handle_start(update: Update, context: CallbackContext) -> None:
    full_name = update.effective_user.full_name
    username = update.effective_user.username
    greeting_name = ''

    if full_name is not None:
        greeting_name = f", {full_name}"
    elif username is not None:
        greeting_name = f", {username}"

    await update.message.reply_text(GREETING.format(greeting_name=greeting_name))


async def handle_togo_to(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Я получил запрос того-то")


async def handle_vot_eto(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Я получил запрос на вот это")
