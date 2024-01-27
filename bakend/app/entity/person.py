class Person:

    def __init__(self, email, password, username=None):
        self.email = email
        self.password = password
        self.username = username
        self.user_id = None


class User(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.calendar = None
        self.currency = None
