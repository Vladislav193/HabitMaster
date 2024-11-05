from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    habit = Column(String, nullable=False)
    frequency = Column(String)
    last_checed = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow())