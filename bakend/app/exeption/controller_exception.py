class DuplicationException(Exception):
    status_code = 400

    def __init__(self, target):
        self.message = f"duplicated {target}"


class ValidationException(Exception):
    status_code = 400

    def __init__(self, target):
        self.message = f"invalid {target}"
