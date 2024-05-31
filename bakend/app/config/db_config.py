from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

engine = db.create_engine("sqlite:///jibi_database.sqlite")

conn = engine.connect()
Base = declarative_base()
