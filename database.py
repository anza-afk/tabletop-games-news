import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from dotenv import load_dotenv
load_dotenv()

# DB = os.environ.get('DB_URL')
# engine = create_engine(DB, echo=True)

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_USER = os.environ.get('POSTGRES_USER')

engine = create_engine(
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}', echo=True
)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

Base.query = Session.query_property()


def migrate():
    Base.metadata.create_all(engine)


def drop():
    Base.metadata.drop_all(engine)


def get_session():
    return Session()


if __name__ == '__main__':
    migrate()
