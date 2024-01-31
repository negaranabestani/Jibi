import unittest

from app.db.database_connectivity import create_record, category_exist, record_exist_id
from app.controller.record_controller import remove_record, add_record, add_category
from app.controller.user_controller import sign_up, generate_token
from app.entity.record import Record, User, Category
from app.exception.controller_exception import ValidationException, DuplicationException

class User_controller_test(unittest.TestCase):
       
    # add user
    def test_should_returnUser_when_addedSuccessfully(self):
        user = User(email='negar@gmail.com', password='123456', username= 'negar')
        result =  sign_up(user)
        self.assertIsNotNone(result)

    def test_should_raiseDuplicationError_when_emailIsDuplicate(self):
        user = User(email='negar@gmail.com', password='123456', username= 'negar')
        self.assertRaises(DuplicationException, sign_up(user))

    
class Record_controller_test(unittest.TestCase):
    
    # add category 
    def test_should_returnCategory_when_addedSuccessfully(self):
        category = Category(color = 'red', icon='circle', title='food', user_id=1)
        result = add_category(category)
        self.assertIsNotNone(result)
    
    def test_should_raiseDuplicationError_when_categoryNameIsReplicate(self):
        category = Category(color = 'red', icon='circle', title='food', user_id=1)
        self.assertRaises(DuplicationException, add_category(category))

    #remove record
    def test_should_raiseValidationError_when_recordDoesntExist(self):
        rid = 0
        self.assertRaises(ValidationException, remove_record(rid))

    #add record
    def test_should_returnAddedRecord_when_addRecordSuccessfull(self):
        record = Record(amount=20, category = 1, date='1/30/2024', title='record1', user_id=1)
        result = add_record(record, 1)
        self.assertIsNotNone(result)

    def test_should_raiseDuplicationError_when_recordNameIsReplicate(self):
        record = Record(amount=20, category=1, date='1/30/2024', title='record1', user_id=1)
        self.assertRaises(DuplicationException, add_record(record, 1))

    def test_should_raiseValidationError_when_categoryNotProvided(self):
        record = Record(amount=20, date='1/30/2024', title='record1', user_id=1, category=None)
        self.assertRaises(ValidationException, add_record(record, 1))


    def test_should_raiseValidationError_when_categoryDoesntExist(self):
        record = Record(amount=20, category= 0, date='1/30/2024', title='record1', user_id=1)
        self.assertRaises(ValidationException, add_record(record, 1))

 




if __name__ == '__main__':
    unittest.main()
