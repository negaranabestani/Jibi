from app.dp.database_connectivity import * 

def should_returnRecord_when_recordSuccessfullyAdded():
    amount = 20 
    uid = 'realID'
    date = '1/30/2024'
    record = Record(amount = amount, date=date, user_id = uid)
    result = create_record(record)
    assert result == record

def should_failAddingRecord_when_dateNotProvided():
    amount = 20 
    uid = 'realID'
    record = Record(amount = amount, user_id = uid)
    result = create_record(record)
    assert result != record

def should_failAddingRecord_when_amountNotProvided():
    amount = 20 
    uid = 'realID'
    date = '1/30/2024'
    record = Record(amount = amount, user_id = uid)
    result = create_record(record)
    assert result != record

def should_failAddingRecord_when_uidNotProvided():
    date = '1/30/2024'
    record = Record(amount = amount, user_id = uid)
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










