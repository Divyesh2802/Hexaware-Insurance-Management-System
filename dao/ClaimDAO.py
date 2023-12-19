from entity.Claim import Claim


class ClaimDAO(Claim):
    def __init__(self):
        super().__init__()

    def perform_claim_actions(self):
        while True:
            print("(Claim) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_claim_table()
            elif ch == 2:
                print(self.add_claim())
            elif ch == 3:
                print(self.update_claim())
            elif ch == 4:
                print(self.delete_claim())
            elif ch == 5:
                self.select_claim()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_claim_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Claim (
            claimId INT PRIMARY KEY,
            claimNumber INT,
            dateFiled DATE,
            claimAmount FLOAT,
            status VARCHAR(50),
            policyId INT,
            clientId INT,
            FOREIGN KEY(policyId) REFERENCES Policy(policyId) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(clientId) REFERENCES Client(clientId) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Claim Table Created successfully.')
        except Exception as e:
            print(e)

    def add_claim(self):
        try:
            self.open()
            self.claimId = int(input('Enter Claim ID: '))
            self.claimNumber = int(input('Enter Claim Number: '))
            self.dateFiled = input('Enter Date Filed: ')
            self.claimAmount = float(input('Enter Claim Amount: '))
            self.status = input('Enter Status: ')
            self.policyId = int(input('Enter Policy ID: '))
            self.clientId = int(input('Enter Client ID: '))
            data = [(self.claimId, self.claimNumber, self.dateFiled, self.claimAmount, self.status, self.policyId, self.clientId)]
            insert_str = '''INSERT INTO Claim(claimId, claimNumber, dateFiled, claimAmount, status, policyId, clientId)
                            VALUES(%s, %s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_claim(self):
        try:
            self.open()
            claim_id = int(input('Enter Claim ID to be Updated: '))
            self.claimNumber = int(input('Enter Claim Number: '))
            self.dateFiled = input('Enter Date Filed: ')
            self.claimAmount = float(input('Enter Claim Amount: '))
            self.status = input('Enter Status: ')
            self.policyId = int(input('Enter Policy ID: '))
            self.clientId = int(input('Enter Client ID: '))
            data = [(self.claimNumber, self.dateFiled, self.claimAmount, self.status, self.policyId, self.clientId, claim_id)]
            update_str = '''UPDATE Claim SET claimNumber=%s, dateFiled=%s, claimAmount=%s, status=%s, policyId=%s, clientId=%s
                            WHERE claimId = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_claim(self):
        try:
            self.open()
            claim_id = int(input('Input Claim ID to be Deleted: '))
            delete_str = f'''DELETE FROM Claim WHERE claimId = {claim_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_claim(self):
        try:
            select_str = '''SELECT * FROM Claim'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Claim Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
