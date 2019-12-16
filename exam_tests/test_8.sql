/*
Given the following data definition, write a query that return names of employees who have no sales.

TABLE employees
    id INTEGER NOT NULL PRIMARY KEY
    name VARCHAR(30) NOT NULL

TABLE sales
    employeeId INTEGER NOT NULL references employees(id)
    value INTEGER NOT NULL CHECK(value > 0)
*/

SELECT names AS 'Employees'
FROM employees
WHERE id NOT IN
(SELECT employeeId FROM sales WHERE value > 0)
