from util.DBConnUtil import DBConnection


class Policy(DBConnection):
    def __init__(self):
        super().__init__()
        self.policyId = 0
        self.policyName = ''

    # SETTERS
    def set_policyId(self, value):
        self.policyId = value

    def set_policyName(self, value):
        self.policyName = value

    # GETTERS
    def get_policyId(self):
        return self.policyId

    def get_policyName(self):
        return self.policyName

    def __str__(self):
        return f'Policy ID: {self.policyId} Policy Name: {self.policyName}'
