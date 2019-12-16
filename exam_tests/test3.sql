/*
Given the following data definition, write a query that selects all customer names together with the number
of transactions that they made. Custormers with no transactions should be included as customer with 0
transactions

TABLE customers
    id INTEGER NOT NULL PRIMARY KEY
    name VARCHAR(30) NOT NULL

TABLE transactions
    id INTEGER NOT NULL PRIMARY KEY
    customerId INTEGER references customers(id)
    amount DECIMAL(15,2) NOT NULL
*/
SELECT customers.name AS 'Customer Name', COUNT()
FROM customers, transactions
WHERE id IN
(SELECT customerId FROM transactions WHERE amount > 0)
