from sqlalchemy import create_engine, Column, Integer, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, unique=True, nullable=False, index=True)
    username = Column(String(255))
    full_name = Column(String(255))
    role = Column(String(10))


class Database:
    def __init__(self, config):
        self.user = config.DB_USER
        self.password = config.DB_PASS
        self.database = config.DB_NAME
        self.host = config.DB_HOST
        self.port = config.DB_PORT

        self.engine = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )
        self.Session = sessionmaker(bind=self.engine)

    def init_db(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()
