class ControllerException(Exception):
    def __init__(self, status_code, target):
        self.status_code = status_code
        self.target = target
        self.message = None


class DuplicationException(ControllerException):
    def __init__(self, target):
        super().__init__(400, target)
        self.message = f"duplicated {target}"


class ValidationException(ControllerException):
    def __init__(self, target):
        super().__init__(400, target)
        self.message = f"invalid {target}"

