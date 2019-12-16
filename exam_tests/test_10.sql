/*
Customers and their orders are stored in the following two tables

TABLE customers
    id INTEGER NOT NULL PRIMARY KEY
    name VARCHAR(50)
    balance DECIMAL(10,2)

TABLE orders
    id INTEGER NOT NULL PRIMARY KEY
    customerId INTEGER NOT NULL REFERENCES customers(id)
    product VARCHAR(50)

Delete the orders of any customer whose balance is negative
*/

DELETE FROM orders
WHERE customerId IN
(SELECT id FROM customers WHERE balance < 0)
