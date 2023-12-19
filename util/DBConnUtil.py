import sys
import mysql.connector as sql
from util.DBPropertyUtil import PropertyUtil


class DBConnection:
    def open(self):
        try:
            # print('--Database Is Connected:--')
            connection_properties = PropertyUtil.getConnectionString()
            self.conn = sql.connect(**connection_properties)
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(str(e) + ' --Database Is Not Connected:--')
            sys.exit(1)

    def close(self):
        self.conn.close()
        # print('--Connection Is Closed:--')
