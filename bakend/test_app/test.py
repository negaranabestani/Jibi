import unittest

from app.db.database_connectivity import create_record, category_exist, record_exist_id
from bakend.app.controller.record_controller import remove_record, add_record
from app.exception import *
from backend.app.entity.record import Record



class database_connectivity_test(unittest.TestCase):

    def test_should_returnRecord_when_recordSuccessfullyAdded(self):
        amount = 20
        uid = 1
        date = '1/30/2024'
        record = Record(amount=amount, date=date, user_id=uid, category=None, title=None)
        result = create_record(record)
        self.assertEqual(result, record)

    def test_should_failAddingRecord_when_dateNotProvided(self):
        amount = 20
        uid = 1
        record = Record(amount=amount, user_id=uid, title=None, category=None, date=None)
        result = create_record(record)
        self.assertNotEqual(result, record)

    def test_should_failAddingRecord_when_amountNotProvided(self):
        uid = 1
        date = '1/30/2024'
        record = Record(date=date, user_id=uid, title=None, category=None, amount=None)
        result = create_record(record)
        self.assertNotEqual(result, record)

    def test_should_failAddingRecord_when_uidNotProvided(self):
        amount = 20
        date = '1/30/2024'
        record = Record(amount=amount, date=date, title=None, category=None, user_id=None)
        result = create_record(record)
        self.assertNotEqual(result, record)

    def test_should_returnTrue_when_recordExists(self):
        result = record_exist_id(1)
        self.assertEqual(result, True)

    def test_should_returnFalse_when_recordDoesntExist(self):
        result = record_exist_id(0)
        self.assertEqual(result, False)

    def test_should_returnTrue_when_categoryExistsAndValidID(self):
        result = category_exist('food', 1)
        assert result == True

    def test_should_returnFalse_when_categoryDoesntExist(self):
        result = category_exist('random', 1)
        assert result == False

    def test_should_returnFalse_when_invalidUserID(self):
        result = category_exist('food', 0)
        self.assertEqual(result, False)


class Record_controller_test(unittest.TestCase):

    
    def test_should_raiseValidationError_when_recordDoesntExist(self):
        rid = 0
        
        with self.assertRaises(ValidationException) as context:
            remove_record(rid)
        self.assertTrue('invalid record_id' in str(context.exception))


    def test_should_returnAddedRecord_when_addRecordSuccessfull(self):
        record = Record(amount=20, category = 1, date='1/30/2024', title='record1', user_id=1)
        result = add_record(record, 1)
        self.assertEqual(result, record)

    def test_should_raiseDuplicationError_when_recordNameIsReplicate(self):
        record = Record(amount=20, category=1, date='1/30/2024', title='record1', user_id=1)
        
        with self.assertRaises(DuplicationException) as context:
            add_record(record, 1)
        self.assertTrue('duplicated record name' in str(context.exception))

    def test_should_raiseValidationError_when_categoryNotProvided(self):
        record = Record(amount=20, date='1/30/2024', title='record1', user_id=1, category=None)

        with self.assertRaises(ValidationException) as context:
            add_record(record, 1)
        self.assertTrue('invalid category_id' in str(context.exception))


    def test_should_raiseValidationError_when_categoryDoesntExist(self):
        record = Record(amount=20, category= 0, date='1/30/2024', title='record1', user_id=1)
        
        with self.assertRaises(ValidationException) as context:
            add_record(record, 1)
        self.assertTrue('invalid category_id' in str(context.exception))
 




if __name__ == '__main__':
    unittest.main()
