from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .command_handlers import handle_start, handle_my_role
from .message_handlers import handle_message
from .database import Database


def create_bot_application(config):
    database = Database(config)
    database.init_db()
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(
        CommandHandler("start", lambda update, context: handle_start(update, context, database))
    )
    application.add_handler(
        CommandHandler("my_role", lambda update, context: handle_my_role(update, context, database))
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    return application
