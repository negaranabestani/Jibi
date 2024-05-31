import os.path
import subprocess
import unittest
from bakend.app.controller.record_controller import remove_record, add_record, add_category
from bakend.app.controller.user_controller import sign_up, generate_token
from bakend.app.entity.category import Category
from bakend.app.entity.person import User
from bakend.app.entity.record import Record
from bakend.app.exception.controller_exception import ValidationException, DuplicationException
from bakend.app.config.db_config import *
from bakend.app.config.logger import jibi_logger
from bakend.app.config import db_config


class User_controller_test(unittest.TestCase):

    # add user
    def test_should_returnUser_when_addedSuccessfully(self):
        # engine = db.create_engine("sqlite:///jibi_database1.sqlite")
        # conn = engine.connect()
        # db_config.engine = engine
        Base.metadata.create_all(engine)
        user = User(email='negar@gmail.com', password='123456', username='negar')
        result = sign_up(user)
        subprocess.run(["rm", "jibi_database.sqlite"])
        self.assertIsNotNone(result)

#     def test_should_raiseDuplicationError_when_emailIsDuplicate(self):
#         engine = db.create_engine("sqlite:///jibi_database2.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         # TODO use this pattern in others if needed previous doesn't work
#         p = False
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         try:
#             sign_up(user)
#             sign_up(user)
#         except DuplicationException:
#             p = True
#         subprocess.run(["rm", "jibi_database2.sqlite"])
#         self.assertTrue(p)
#
#
# class Record_controller_test(unittest.TestCase):
#
#     # add category
#     def test_should_returnCategory_when_addedSuccessfully(self):
#         engine = db.create_engine("sqlite:///jibi_database3.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         # ToDo user id is required
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         sign_up(user)
#         category = Category(color='red', icon='circle', title='food', user_id=1)
#         result = add_category(category, 1)
#         subprocess.run(["rm", "jibi_database3.sqlite"])
#         self.assertIsNotNone(result)
#
#     # def test_should_raiseDuplicationError_when_categoryNameIsReplicate(self):
#     #     user = User(email='negar@gmail.com', password='123456', username='negar')
#     #     sign_up(user)
#     #     category = Category(color='red', icon='circle', title='food', user_id=1)
#     #     category1 = Category(color='red', icon='icon1', title='food', user_id=1)
#     #     p = False
#     #     try:
#     #         add_category(category, 1)
#     #         add_category(category1, 1)
#     #     except DuplicationException:
#     #         p = True
#     #     subprocess.run(["rm", "jibi_database.sqlite"])
#     #     self.assertTrue(p)
#
#     # remove record
#     def test_should_raiseValidationError_when_recordDoesntExist(self):
#         engine = db.create_engine("sqlite:///jibi_database4.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         rid = 0
#         p = False
#         try:
#             remove_record(rid)
#         except ValidationException:
#             p = True
#         subprocess.run(["rm", "jibi_database4.sqlite"])
#         self.assertTrue(p)
#
#     # add record
#     def test_should_returnAddedRecord_when_addRecordSuccessfull(self):
#         engine = db.create_engine("sqlite:///jibi_database5.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         sign_up(user)
#         category = Category(color='red', icon='circle', title='food', user_id=1)
#         add_category(category, 1)
#         record = Record(amount=20, category=1, date='1/30/2024', title='record1', user_id=1, type="Expense")
#         result = add_record(record, 1)
#         subprocess.run(["rm", "jibi_database5.sqlite"])
#         self.assertIsNotNone(result)
#
#     def test_should_raiseDuplicationError_when_recordNameIsReplicate(self):
#         engine = db.create_engine("sqlite:///jibi_database6.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         sign_up(user)
#         category = Category(color='red', icon='circle', title='food', user_id=1)
#         add_category(category, 1)
#         record = Record(amount=20, category=1, date='1/30/2024', title='record1', user_id=1, type="Expense")
#         p = False
#         try:
#             add_record(record, 1)
#             add_record(record, 1)
#         except DuplicationException:
#             p = True
#         subprocess.run(["rm", "jibi_database6.sqlite"])
#         self.assertTrue(p)
#
#     def test_should_raiseValidationError_when_categoryNotProvided(self):
#         engine = db.create_engine("sqlite:///jibi_database7.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         sign_up(user)
#         category = Category(color='red', icon='circle', title='food', user_id=1)
#         add_category(category, 1)
#         record = Record(amount=20, date='1/30/2024', title='record1', user_id=1, category=None, type="Expense")
#         p = False
#         try:
#             add_record(record, 1)
#         except ValidationException:
#             p = True
#         subprocess.run(["rm", "jibi_database7.sqlite"])
#         self.assertTrue(p)
#
#     def test_should_raiseValidationError_when_categoryDoesntExist(self):
#         engine = db.create_engine("sqlite:///jibi_database8.sqlite")
#         conn = engine.connect()
#         db_config.engine = engine
#         Base.metadata.create_all(engine)
#         user = User(email='negar@gmail.com', password='123456', username='negar')
#         sign_up(user)
#         category = Category(color='red', icon='circle', title='food', user_id=1)
#         add_category(category, 1)
#         record = Record(amount=20, category=0, date='1/30/2024', title='record1', user_id=1, type="Expense")
#         p = False
#         try:
#             add_record(record, 1)
#         except ValidationException:
#             p = True
#         subprocess.run(["rm", "jibi_database8.sqlite"])
#         self.assertTrue(p)


if __name__ == '__main__':
    unittest.main()
