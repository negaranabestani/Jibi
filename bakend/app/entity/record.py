import sys

sys.path.append('../../')
from app.config.db_config import Base
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Double, ForeignKey


class Record(Base):
    __tablename__ = 'records'
    amount = Column(Double)
    category_id = Column(ForeignKey("categories.id"))
    date = Column(String(40))
    title = Column(String(40))
    type = Column(String(40))
    user_id = Column(ForeignKey("users.user_id"))
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, amount, category, date, title, user_id, type):
        self.amount = amount
        self.category_id = category
        self.date = date
        self.title = title
        self.user_id = user_id
        self.type = type
        self.id = None
