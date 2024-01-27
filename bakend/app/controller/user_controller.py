import uuid


def login(email, password):
    valid = True
    user_id = ""
    # ToDo check input validity form database
    return generate_token(user_id)


def generate_token(user_id):
    return user_id + str(uuid.uuid4())
