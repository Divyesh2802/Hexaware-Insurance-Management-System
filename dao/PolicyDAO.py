from entity.Policy import Policy


class PolicyDAO(Policy):
    def __init__(self):
        super().__init__()

    def perform_policy_actions(self):
        while True:
            print("(Policy) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_policy_table()
            elif ch == 2:
                print(self.add_policy())
            elif ch == 3:
                print(self.update_policy())
            elif ch == 4:
                print(self.delete_policy())
            elif ch == 5:
                self.select_policy()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_policy_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Policy (
            policyId INT PRIMARY KEY,
            policyName VARCHAR(50))'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Policy Table Created successfully.')
        except Exception as e:
            print(e)

    def add_policy(self):
        try:
            self.open()
            self.policyId = int(input('Enter Policy ID: '))
            self.policyName = input('Enter Policy Name: ')
            data = [(self.policyId, self.policyName)]
            insert_str = '''INSERT INTO Policy(policyId, policyName)
                            VALUES(%s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_policy(self):
        try:
            self.open()
            policy_id = int(input('Input Policy ID to be Updated: '))
            self.policyName = input('Enter Policy Name: ')
            data = [(self.policyName, policy_id)]
            update_str = '''UPDATE Client SET policyName=%s
                            WHERE policyId = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_policy(self):
        try:
            self.open()
            policy_id = int(input('Input Policy ID to be Deleted: '))
            delete_str = f'''DELETE FROM Policy WHERE policyId = {policy_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_policy(self):
        try:
            select_str = '''SELECT * FROM Policy'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Policy Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)

    def getPolicy(self, policyId):
        pass

    def getAllPolicies(self):
        pass
