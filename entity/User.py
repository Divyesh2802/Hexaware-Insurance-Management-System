from util.DBConnUtil import DBConnection


class User(DBConnection):
    def __init__(self):
        super().__init__()
        self.userId = 0
        self.userName = ''
        self.password = ''
        self.role = ''

    # SETTERS
    def set_userId(self, value):
        self.userId = value

    def set_userName(self, value):
        self.userName = value

    def set_password(self, value):
        self.password = value

    def set_role(self, value):
        self.role = value

    # GETTERS
    def get_userId(self):
        return self.userId

    def get_userName(self):
        return self.userName

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def __str__(self):
        return f'User ID: {self.userId} User Name: {self.userName} Role: {self.role}'
