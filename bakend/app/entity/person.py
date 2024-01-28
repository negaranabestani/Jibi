from app.db.database_connectivity import Base
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String


class Person:

    def __init__(self, email, password, username=None):
        self.email = email
        self.password = password
        self.username = username
        self.user_id = None


class User(Person, Base):
    __tablename__ = 'users'
    email = Column(String(40))
    password = Column(String(20))
    username = Column(String(40), nullable=True)
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    calendar = Column(String(40), nullable=True)
    currency = Column(String(40), nullable=True)

    def __init__(self, email, password):
        super().__init__(email, password)
        self.calendar = None
        self.currency = None
