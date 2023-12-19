from entity.Client import Client


class Payment(Client):
    def __init__(self):
        super().__init__()
        self.paymentId = 0
        self.paymentDate = ''
        self.paymentAmount = 0.0
        self.clientId = 0

    # SETTERS
    def set_paymentId(self, value):
        self.paymentId = value

    def set_paymentDate(self, value):
        self.paymentDate = value

    def set_paymentAmount(self, value):
        self.paymentAmount = value

    def set_clientId(self, value):
        self.clientId = value

    # GETTERS
    def get_paymentId(self):
        return self.paymentId

    def get_paymentDate(self):
        return self.paymentDate

    def get_paymentAmount(self):
        return self.paymentAmount

    def get_clientId(self):
        return self.clientId

    def __str__(self):
        return f'Payment ID: {self.paymentId} Payment Date: {self.paymentDate} Payment Amount: {self.paymentAmount}\n' \
               f' Client ID: {self.clientId}'
