class PropertyUtil:
    connection_properties = None

    @staticmethod
    def getConnectionString():
        if PropertyUtil.connection_properties is None:
            host = input('Enter the database host: ')
            database = input('Enter the database name: ')
            user = input('Enter the database user: ')
            password = input('Enter the database password: ')
            PropertyUtil.connection_properties = {'host': host, 'database': database, 'user': user, 'password': password}
        return PropertyUtil.connection_properties
