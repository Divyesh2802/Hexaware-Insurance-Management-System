from entity.Client import Client


class Claim(Client):
    def __init__(self):
        super().__init__()
        self.claimId = 0
        self.claimNumber = 0
        self.dateFiled = ''
        self.claimAmount = 0.0
        self.status = ''
        self.policyId = ''
        self.clientId = 0

    # SETTERS
    def set_claimId(self, value):
        self.claimId = value

    def set_claimNumber(self, value):
        self.claimNumber = value

    def set_dateFiled(self, value):
        self.dateFiled = value

    def set_claimAmount(self, value):
        self.claimAmount = value

    def set_status(self, value):
        self.status = value

    def set_policyId(self, value):
        self.policyId = value

    def set_clientId(self, value):
        self.clientId = value

    # GETTERS
    def get_claimId(self):
        return self.claimId

    def get_claimNumber(self):
        return self.claimNumber

    def get_dateFiled(self):
        return self.dateFiled

    def get_claimAmount(self):
        return self.claimAmount

    def get_status(self):
        return self.status

    def get_policyId(self):
        return self.status

    def get_clientId(self):
        return self.clientId

    def __str__(self):
        return f'Claim ID: {self.claimId} Claim Number: {self.claimNumber}\n' \
               f'Date Filed: {self.dateFiled} Claim Amount: {self.claimAmount} Status: {self.status}\n' \
               f'Policy ID: {self.policyId} Client ID: {self.clientId}'
