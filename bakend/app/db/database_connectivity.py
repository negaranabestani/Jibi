import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine("sqlite:///jibi_database.sqlite")

conn = engine.connect()
Base = declarative_base(bind=engine)
