from sqlalchemy import *
from sqlalchemy.orm import Session
import sys

sys.path.append('../../')
from app.entity.record import *
from app.entity.person import *
from app.entity.category import *
from app.config.db_config import *
from app.config.logger import jibi_logger

Base.metadata.create_all(engine)


def select_records(user_id: str):
    session = Session(engine)
    s = select(Record).where(Record.user_id == user_id)
    session.commit()
    return session.scalars(s).all()


def create_record(record: Record):
    session = Session(engine)
    # record.category_id=record.category
    session.add(record)
    s = select(Record).where(Record.user_id == record.user_id).where(Record.title == record.title)
    session.commit()
    return session.scalars(s).first()


def update_record(record: Record):
    session = Session(engine)
    # update(Record).where(Record.id == record.id).values(title=record.title, amount=record.amount,
    #                                                     category_id=record.category)
    session.query(Record).filter(Record.id == record.id).update(
        {"title": record.title, "amount": record.amount, "category_id": record.category_id})
    s = select(Record).where(Record.id == record.id)
    session.commit()
    return session.scalars(s).first()


def delete_record(record_id):
    session = Session(engine)
    # delete(Record).where(Record.id == record_id)
    session.query(Record).filter(Record.id == record_id).delete()
    session.commit()


def create_user(user: User):
    session = Session(engine)
    session.add(user)
    s = select(User).where(User.email == user.email)
    # s=session.query(User).filter_by(email="ed").first()
    session.commit()
    return session.scalars(s).first()


def update_user(user: User):
    session = Session(engine)
    # update(User).where(User.user_id == user.user_id).values(username=user.username, calendar=user.calendar,
    #                                                         currency=user.currency, password=user.password)
    session.query(User).filter(User.user_id == user.user_id).update(
        {"username": user.username, "calendar": user.calendar, "currency": user.currency, "password": user.password})
    session.commit()
    s = select(User).where(User.user_id == user.user_id)
    return session.scalars(s).first()


def get_user(email, password):
    session = Session(engine)
    s = select(User).where(User.email == email).where(User.password == password)
    session.commit()
    res = session.scalars(s).first()
    # jibi_logger.info(password)
    return res


def select_categories(user_id: int):
    session = Session(engine)
    s = select(Category).where(Category.user_id == user_id)
    session.commit()
    return session.scalars(s).all()


def create_category(cat: Category):
    session = Session(engine)
    session.add(cat)
    s = select(Category).where(Category.user_id == cat.user_id).where(Category.title == cat.title)
    session.commit()
    return session.scalars(s).first()


def get_category(cat_id):
    session = Session(engine)
    s = select(Category).where(Category.id == cat_id)
    return session.scalars(s).first()

def get_record(record_id):
    session = Session(engine)
    s = select(Record).where(Record.id == record_id)
    return session.scalars(s).first()
def update_category(cat: Category):
    session = Session(engine)

    # update(Category).where(Category.id == cat.id).values(color=cat.color, icon=cat.icon, title=cat.title)
    session.query(Category).filter(Category.id == cat.id).update(
        {"color": cat.color, "icon": cat.icon, "title": cat.title})
    session.commit()
    s = select(Category).where(Category.id == cat.id)
    return session.scalars(s).first()


def delete_category(cat_id):
    session = Session(engine)
    # session.delete(Category).where(Category.id == cat_id)
    session.query(Category).filter(Category.id == cat_id).delete()
    session.commit()


def user_exist(email):
    session = Session(engine)
    s = select(User.email)
    session.commit()
    result = session.scalars(s)
    if email in result:
        return True
    return False


def record_exist(title, user_id):
    session = Session(engine)
    s = select(Record.title).where(Record.user_id == user_id)
    session.commit()
    result = session.scalars(s)
    if title in result:
        return True
    return False


def category_exist(title, user_id):
    session = Session(engine)
    s = select(Category.title).where(Category.user_id == user_id or Category.user_id == "golbal")
    session.commit()
    result = session.scalars(s)
    if title in result:
        return True
    return False


def category_exist_id(id):
    session = Session(engine)
    s = select(Category.id)
    session.commit()
    result = session.scalars(s)
    if id in result:
        return True
    return False


def record_exist_id(id):
    session = Session(engine)
    s = select(Record.id)
    session.commit()
    result = session.scalars(s)
    if id in result:
        return True
    return False


def category_empty():
    session = Session(engine)
    s = select(Category)
    session.commit()
    result = session.scalars(s)
    if len(result.all()) == 0:
        return True
    return False
