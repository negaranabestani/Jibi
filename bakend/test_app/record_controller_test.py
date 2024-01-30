
from app.controller.record_controller import *

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




