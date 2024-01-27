class Person:

    def __init__(self, email, password, username=None):
        self.email = email
        self.password = password
        self.username = username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username

    def set_password(self, new_password):
        self.password = new_password

    def set_username(self, new_username):
        self.username = new_username


class User(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.calendar = None
        self.currency = None

    def get_calendar(self):
        return self.calendar

    def get_currency(self):
        return self.currency

    def set_calendar(self, new_calendar):
        self.calendar = new_calendar

    def set_currency(self, new_currency):
        self.currency = new_currency
