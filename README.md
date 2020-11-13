# CS627_SQL
SQL with Python Project Repository

## Schema
![Schema](https://github.com/ViswanathanAR96/CS627_SQL/blob/maseter_v2/Drawing1.jpg)

## Reducing Schema to Entity Relationship
- Product (prodId, pname, price)
- Depot (depId, addr, volume)
- Stock (prodId, depId, quantity)

### Algorithm
- 	Product has Stock (1N):\
    Stock (quantity, depId)\
    *Since prodId is the PK(Product) and FK(Stock) - > Removing prodId from the Stock table*\
    Product (prodId, pname, price)
- 	Stock stored in Depot (N1)\
    Stock (quantity)\
    *Since depId is the PK(Depot) and FK(Stock) -> Removing depId from Stock Table*\
    Depot(depId, addr, volume)

### Entity Relationship
- Product (prodId, pname, price), PK = prodId
- Depot (depId, addr, volume), PK = depId
- Stock (quantity)

## ER Diagram
![ER Diagram](https://github.com/ViswanathanAR96/CS627_SQL/blob/maseter_v2/ERDiagram.jpg)

## About
A pythonic implementation of Database transactions using Psycopg2 as the ORM.

### To run the Project
1. Clone the project, and open it in your favourite text editor
2. To run the project, change the directory to the root direcory of this repository
3. Run '.venv/Scripts/activate.bat' to activate the virtual environment
4. Perform the following operations:
    - Open psql
    - Provide the credentials
    - Create database test_db
    - Run "CREATE TABLE Products (prod_id VARCHAR(5), pname VARCHAR(50), price INTEGER);"
    - Run "ALTER TABLE Products ADD CONSTRAINT pk_Product_prodid PRIMARY KEY (prod_id);"
    - Run "CREATE TABLE Depot (dep_id VARCHAR(5), addr VARCHAR(50), volume INTEGER);"
    - Run "ALTER TABLE Depot ADD CONSTRAINT pk_Depot_depid PRIMARY KEY (dep_id);"
    - Run "CREATE TABLE Stock (prod_id VARCHAR(5), dep_id VARCHAR(5), quantity INTEGER);"
    - Run "ALTER TABLE Stock ADD CONSTRAINT fk_Stock_prodid FOREIGN KEY (prod_id)  REFERENCES Products(prod_id);"
    - Run "ALTER TABLE Stock ADD CONSTRAINT fk_Stock_depid FOREIGN KEY (dep_id)  REFERENCES Depot(dep_id);"
    - Run "INSERT INTO  Products VALUES ('p1', 'tape', 2.5);"
    - Run "INSERT INTO  Products VALUES ('p2', 'tv', 250);"
    - Run "INSERT INTO  Products VALUES ('p3', 'vcr', 80);"
    - Run "INSERT INTO  Depot VALUES ('d1', 'New York', 9000);"
    - Run "INSERT INTO  Depot VALUES ('d2', 'Syracuse', 6000);"
    - Run "INSERT INTO  Depot VALUES ('d4', 'New York', 2000);"
    - Run "INSERT INTO  Stock VALUES ('p1', 'd1', 1000);"
    - Run "INSERT INTO  Stock VALUES ('p1', 'd2', -100);"
    - Run "INSERT INTO  Stock VALUES ('p1', 'd4', 1200);"
    - Run "INSERT INTO  Stock VALUES ('p3', 'd1', 3000);"
    - Run "INSERT INTO  Stock VALUES ('p3', 'd4', 2000);"
    - Run "INSERT INTO  Stock VALUES ('p2', 'd4', 1500);"
    - Run "INSERT INTO  Stock VALUES ('p2', 'd1', -400);"
    - Run "INSERT INTO  Stock VALUES ('p2', 'd2', 2000);"
5. Update the credentials in Transactions.py and run class Transaction in Transaction.py

### Working
There are two python files. Pysql.py contains SQLConnect class which has methods to open and close connection to database. Transaction.py contains Transaction.class which contains two methods to initiate the updating of Stock and Products table. And, another method to print  records from the Stock and Products table.

#### Statement: The product p1 changes its name to pp1 in Product and Stock.
The transaction should be consistent and atomic before, on and after running the following transactions
1. Remove the fk_Stock_prodid constraint from Stock Table
2. Update Products table with p1 = pp1
3. Update stock table with p1 = pp1
4. Add fk_Stock_prodid constraint from Stock Table  
The ACID properties of the transaction is managed here by setting autocommit = False, then executig the above transactions, committing the transacions to the datbase if there are no exceptions/errors. If htere are error(s), rollback the transaction o previous state.  
On running the select query, the transaction's validity could be verified.
    

