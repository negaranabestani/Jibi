
from app.controller.record_controller import *
from app.dp.database_connectivity import * 
from app.entity import *
import unittest

class Record_controller_test(unittest.TestCase):

    def should_raiseValidationError_when_recordDoesntExist():
        rid = 'invalidID'
        result = delete_record(rid)
        assert result == 'invalid record_id'
        

    def should_returnAddedRecord_when_addRecordSuccessfull():
        record = Record(amount=20, category='food', date='1/30/2024', title='record1', user_id='realID')
        result = add_record(record, 'realID')
        assert result == record

    def should_raiseDuplicationError_when_recordNameIsReplicate():
        record = Record(amount=20, category='food', date='1/30/2024', title='record1', user_id='realID')
        result = add_record(record, 'realID')
        assert result == 'duplicated record name'

    def should_raiseValidationError_when_categoryNotProvided():
        record = Record(amount=20, date='1/30/2024', title='record1', user_id='realID', category= None)
        result = add_record(record, 'realID')
        assert result == 'invalid category_id'

    def should_raiseValidationError_when_categoryDoesntExist():
        record = Record(amount=20, category='random' ,date='1/30/2024', title='record1', user_id='realID')
        result = add_record(record, 'realID')
        assert result == 'invalid category_id'



class database_connectivity_test(unittest.TestCase):

    def should_returnRecord_when_recordSuccessfullyAdded():
        amount = 20 
        uid = 'realID'
        date = '1/30/2024'
        record = Record(amount = amount, date=date, user_id = uid, category = None, title =None)
        result = create_record(record)
        assert result == record

    def should_failAddingRecord_when_dateNotProvided():
        amount = 20 
        uid = 'realID'
        record = Record(amount = amount, user_id = uid, title = None, category = None, date = None)
        result = create_record(record)
        assert result != record

    def should_failAddingRecord_when_amountNotProvided():
        uid = 'realID'
        date = '1/30/2024'
        record = Record(date = date, user_id = uid, title = None, category = None, amount = None)
        result = create_record(record)
        assert result != record

    def should_failAddingRecord_when_uidNotProvided():
        date = '1/30/2024'
        record = Record(amount = amount, date = date, title = None, category = None, user_id = None)
        result = create_record(record)
        assert result != record


    def should_returnTrue_when_recordExists():
        result = record_exist_id('realID')
        assert result == True

    def should_returnFalse_when_recordDoesntExist():
        result = record_exist_id('123456')
        assert result == False

    def should_returnTrue_when_categoryExistsAndValidID():
        result = category_exist('food','realID')
        assert result == True

    def should_returnFalse_when_categoryDoesntExist():
        result = category_exist('random','realID')
        assert result == False

    def should_returnFalse_when_invalidUserID():
        result = category_exist('food', '123456')
        assert result == False


if __name__ == '__main__':
    unittest.main()


