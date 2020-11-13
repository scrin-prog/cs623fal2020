import psycopg2
from Pysql import SQLConnect

class Transaction(SQLConnect):
    def __init__(self, user, password, host, port, database):
        super().__init__(user, password, host, port, database)

    def manageTransaction(self, prodId, upd_ProdId, upd_ProdId2):
        connection, cursor = super().connect()
        connection.autocommit = False
        try:
            cursor.execute("ALTER TABLE Stock DROP CONSTRAINT fk_stock_prodid;")
            cursor.execute(f"UPDATE Products SET prod_id = \'{upd_ProdId}\' WHERE prod_id = \'{prodId}\';")
            cursor.execute(f"UPDATE Stock SET prod_id = \'{upd_ProdId}\' WHERE prod_id = \'{prodId}\';")
            cursor.execute("ALTER TABLE Stock ADD CONSTRAINT fk_stock_prodid FOREIGN KEY (prod_id) REFERENCES Products(prod_id);")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            connection.rollback()
        super().connect_close(connection, cursor)
    
    def selectRecords(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("SELECT prod_id, pname, price from Products")
            rows = cursor.fetchall()
            for r in rows:
                print(f"prod_id: {r[0]}\t name: {r[1]}\t Price:{r[2]}")
            print('\n')
            cursor.execute("SELECT prod_id, dep_id, quantity FROM Stock")
            rows = cursor.fetchall()
            for r in rows:
                print(f"prod_id: {r[0]}\t dep_id: {r[1]}\t Quantity:{r[2]}")
        except(Exception, psycopg2.Error) as error:
            print(error)
        super().connect_close(connection, cursor)

            
v = Transaction(user = "postgres", password = "Quantum1!", host = "127.0.0.1", port = "5432", database = "Inventory")
v.manageTransaction('p1', 'pp1', 'pp2')
v.selectRecords()