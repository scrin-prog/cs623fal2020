import psycopg2
from Pysql import SQLConnect

class Transaction(SQLConnect):
    def __init__(self, user, password, host, port, database):
        super().__init__(user, password, host, port, database)

    def manageTransaction(self, prodId, upd_ProdId, err_param):
        connection, cursor = super().connect()
        connection.autocommit = False
        try:
            cursor.execute("ALTER TABLE Stock DROP CONSTRAINT fk_stock_prodid;")
            cursor.execute("UPDATE Products SET prod_id = \'{0}\' WHERE prod_id = \'{1}';".format(upd_ProdId, prodId))
            cursor.execute("UPDATE Stock SET prod_id = \'{0}\' WHERE prod_id = \'{1}\';".format(upd_ProdId, prodId))
            cursor.execute("ALTER TABLE Stock ADD CONSTRAINT fk_stock_prodid FOREIGN KEY (prod_id) REFERENCES Products(prod_id);")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error: ",error)
            connection.rollback()
        super().connect_close(connection, cursor)
    
    def selectRecords(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("SELECT prod_id, pname, price from Products")
            rows = cursor.fetchall()
            print("**********Products Table***********")
            for r in rows:
                print("prod_id: {0}\t name: {1}\t Price:{2}".format(r[0], r[1], r[2]))
            print('\n')
            cursor.execute("SELECT prod_id, dep_id, quantity FROM Stock")
            rows = cursor.fetchall()
            print("***********Depot Table************")
            for r in rows:
                print("prod_id: {0}\t dep_id: {1}\t Quantity:{2}".format(r[0], r[1], r[2]))
        except(Exception, psycopg2.Error) as error:
            print("Error: ",error)
        super().connect_close(connection, cursor)

            
v = Transaction(user = "postgres", password = "user", host = "127.0.0.1", port = "5432", database = "test_db")
v.manageTransaction('p1', 'pp1', 'pp2')
v.selectRecords()