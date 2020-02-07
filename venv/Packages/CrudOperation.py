from Packages import *

cursor = connect(server, database, username, password)


class CRUD:

    def DisplayTable(self, table_name):
        query = 'select * from ' + table_name + ';'
        table = cursor.execute(query)
        for row in table:
            print(row)

    def Insert(self):
        Insert_query = '''INSERT INTO Customer(FirstName, LastName, Age, City)
                          VALUES(?,?,?,?);'''

        for row in Customer_data:
            values = (row[0], row[1], row[2], row[3])
            cursor.execute(Insert_query, values)

        conn.commit()

# o = CRUD()
# o.DisplayTable('Customer')
