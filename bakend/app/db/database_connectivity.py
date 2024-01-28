import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.entity.record import *
from app.entity.person import *
from app.entity.category import *

engine = db.create_engine("sqlite:///jibi_database.sqlite")

conn = engine.connect()
Base = declarative_base(bind=engine)
Base.metadata.create_all()
session = Session(engine)


def select_records(user_id: str):
    s = select(Record).where(Record.user_id == user_id)
    session.commit()
    return session.scalars(s)


def create_record(record: Record):
    session.add(record)
    s = select(Record).where(Record.user_id == record.user_id and Record.title == record.title)
    session.commit()
    return session.scalars(s)


def update_record(record: Record):
    update(Record).where(Record.id == record.id).values(record)
    s = select(Record).where(Record.id == record.id)
    session.commit()
    return session.scalars(s)


def delete_record(record_id):
    delete(Record).where(Record.id == record_id)
    session.commit()


def create_user(user: User):
    session.add(user)
    s = select(User).where(User.email == user.email)
    session.commit()
    return session.scalars(s)


def update_user(user: User):
    update(User).where(User.user_id == user.user_id).values(user)
    s = select(User).where(User.user_id == user.user_id)
    session.commit()
    return session.scalars(s)


def get_user(email, password):
    s = select(User).where(User.email == email and User.password == password)
    session.commit()
    return session.scalars(s)


def select_categories(user_id: str):
    s = select(Category).where(Category.user_id == user_id)
    session.commit()
    return session.scalars(s)


def create_category(cat: Category):
    session.add(cat)
    s = select(Category).where(Category.user_id == cat.user_id and Category.title == cat.title)
    session.commit()
    return session.scalars(s)


def update_category(cat: Category):
    update(Category).where(Category.id == cat.id).values(cat)
    s = select(Category).where(Category.id == cat.id)
    session.commit()
    return session.scalars(s)


def delete_category(cat_id):
    delete(Category).where(Category.id == cat_id)
    session.commit()


def user_exist(email):
    s = select(User.email)
    session.commit()
    result = session.scalars(s)
    if email in result:
        return True
    return False


def record_exist(title):
    s = select(Record.title)
    session.commit()
    result = session.scalars(s)
    if title in result:
        return True
    return False


def category_exist(title):
    s = select(Category.title)
    session.commit()
    result = session.scalars(s)
    if title in result:
        return True
    return False


def record_exist_id(id):
    s = select(Record.id)
    session.commit()
    result = session.scalars(s)
    if id in result:
        return True
    return False
