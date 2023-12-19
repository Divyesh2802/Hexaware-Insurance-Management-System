from entity.Policy import Policy


class Client(Policy):
    def __init__(self):
        super().__init__()
        self.clientId = 0
        self.clientName = ''
        self.contactInfo = 0
        self.policyId = ''

    # SETTERS
    def set_clientId(self, value):
        self.clientId = value

    def set_clientName(self, value):
        self.clientName = value

    def set_contactInfo(self, value):
        self.contactInfo = value

    def set_policyId(self, value):
        self.policyId = value

    # GETTERS
    def get_clientId(self):
        return self.clientId

    def get_clientName(self):
        return self.clientName

    def get_contactInfo(self):
        return self.contactInfo

    def get_policyId(self):
        return self.policyId

    def __str__(self):
        return f'Client ID: {self.clientId} Client Name: {self.clientName} Contact Info: {self.contactInfo}\n' \
               f' Policy ID: {self.policyId}'
