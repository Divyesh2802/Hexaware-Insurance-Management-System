from entity.Client import Client


class ClientDAO(Client):
    def __init__(self):
        super().__init__()

    def perform_client_actions(self):
        while True:
            print("(Client) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_client_table()
            elif ch == 2:
                print(self.add_client())
            elif ch == 3:
                print(self.update_client())
            elif ch == 4:
                print(self.delete_client())
            elif ch == 5:
                self.select_client()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_client_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Client (
            clientId INT PRIMARY KEY,
            clientName VARCHAR(50),
            contactInfo INT,
            policyId INT,
            FOREIGN KEY(policyId) REFERENCES Policy(policyId) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Client Table Created successfully.')
        except Exception as e:
            print(e)

    def add_client(self):
        try:
            self.open()
            self.clientId = int(input('Enter Client ID: '))
            self.clientName = input('Enter Client Name: ')
            self.contactInfo = int(input('Enter Contact Info: '))
            self.policyId = int(input('Enter Policy ID: '))
            data = [(self.clientId, self.clientName, self.contactInfo, self.policyId)]
            insert_str = '''INSERT INTO Client(clientId, clientName, contactInfo, policyId)
                            VALUES(%s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_client(self):
        try:
            self.open()
            client_id = int(input('Input Client ID to be Updated: '))
            self.clientName = input('Enter Client Name: ')
            self.contactInfo = int(input('Enter Contact Info: '))
            self.policyId = int(input('Enter Policy ID: '))
            data = [(self.clientName, self.contactInfo, self.policyId, client_id)]
            update_str = '''UPDATE Client SET clientName=%s, contactInfo=%s, policyId=%s
                            WHERE clientId = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_client(self):
        try:
            self.open()
            client_id = int(input('Input Client ID to be Deleted: '))
            delete_str = f'''DELETE FROM Client WHERE clientId = {client_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_client(self):
        try:
            select_str = '''SELECT * FROM Client'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Client Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
