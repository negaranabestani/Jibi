import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.entity.record import *
from app.entity.person import *

engine = db.create_engine("sqlite:///jibi_database.sqlite")

conn = engine.connect()
Base = declarative_base(bind=engine)
Base.metadata.create_all()
session = Session(engine)


def get_records(user_id: str):
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
