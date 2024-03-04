from config import Config
from bot import create_bot_application

if __name__ == '__main__':
    config = Config()
    application = create_bot_application(config)
    application.run_polling()
