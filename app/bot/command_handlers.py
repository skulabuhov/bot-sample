from telegram import Update
from telegram.ext import CallbackContext
from .database import Database, User

RETURNING_GREETING_TITLE = "С возвращением{greeting_name}!"
NEW_GREETING_TITLE = "Добро пожаловать{greeting_name}!"
GREETING = """{greeting_title}

Этот бот умеет вот это и вот это

Чтобы посмотреть Вашу роль, выполните команду:
/my_role

Желаем Вам удачи!"""


async def handle_start(update: Update, context: CallbackContext, database: Database) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    full_name = update.effective_user.full_name
    username = update.effective_user.username
    greeting_name = ''

    if full_name is not None:
        greeting_name = f", {full_name}"
    elif username is not None:
        greeting_name = f", {username}"

    with database.get_session() as session:
        user = session.query(User).filter_by(chat_id=chat_id).first()

        if user:
            user.username = username
            user.full_name = full_name
            session.commit()
            await update.message.reply_text(
                GREETING.format(greeting_title=RETURNING_GREETING_TITLE.format(greeting_name=greeting_name))
            )
        else:
            new_user = User(user_id=user_id, chat_id=chat_id, username=username, full_name=full_name, role='user')
            session.add(new_user)
            session.commit()
            await update.message.reply_text(
                GREETING.format(greeting_title=NEW_GREETING_TITLE.format(greeting_name=greeting_name))
            )


async def handle_my_role(update: Update, context: CallbackContext, database: Database) -> None:
    chat_id = update.effective_chat.id

    with database.get_session() as session:
        user = session.query(User).filter_by(chat_id=chat_id).first()

        if user:
            if user.role == "user":
                await update.message.reply_text("Вы - наш любимый пользователь!")
            elif user.role == "admin":
                await update.message.reply_text("Вы - наш могучий админ!")
            else:
                await update.message.reply_text("Мы без понятия кто Вы!")
        else:
            await update.message.reply_text("Вас нет в базе данных!\nВыполните команду /start")