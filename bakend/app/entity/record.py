from app.db.database_connectivity import Base
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Double, ForeignKey


class Record(Base):
    __tablename__ = 'records'
    amount = Column(Double)
    category_id = Column(Integer)
    date = Column(String(40))
    title = Column(String(40))
    user_id = Column(ForeignKey("user.id"))
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, amount, category: None, date, title: None, user_id):
        self.amount = amount
        self.category = category
        self.date = date
        self.title = title
        self.user_id = user_id
        self.id = None
