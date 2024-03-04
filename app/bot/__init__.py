from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .command_handlers import handle_start, handle_togo_to, handle_vot_eto
from .message_handlers import handle_message


def create_bot_application(config):
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(CommandHandler("togo_to", handle_togo_to))
    application.add_handler(CommandHandler("vot_eto", handle_vot_eto))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    return application
