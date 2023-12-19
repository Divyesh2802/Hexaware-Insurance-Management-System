from dao.PolicyDAO import PolicyDAO
from exception.PolicyNotFoundException import PolicyNotFoundException


class InsuranceServiceImpl(PolicyDAO):
    def __init__(self):
        super().__init__()

    # GET ALL POLICIES
    def getAllPolicies(self):
        try:
            self.open()
            self.stmt.execute('''SELECT * FROM Policy''')
            records = self.stmt.fetchall()
            self.close()
            return records
        except Exception as e:
            return e

    # GET POLICY
    def getPolicy(self, policyId):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Policy WHERE policyId = {policyId}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise PolicyNotFoundException(policyId)
            else:
                self.stmt.execute(f'''SELECT * FROM Policy WHERE policyId = {policyId}''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except PolicyNotFoundException as e:
            return e
        except Exception as e:
            return e
