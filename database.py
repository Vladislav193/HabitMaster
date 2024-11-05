import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL =os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bing=engine)
session = Session()
Base = declarative_base

def init_db():
    Base.metadata.create_all(engine)