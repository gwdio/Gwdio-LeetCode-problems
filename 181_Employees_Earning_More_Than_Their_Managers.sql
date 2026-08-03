SELECT e.name as Employee
FROM Employee AS e
RIGHT JOIN (SELECT e.id AS mid, e.salary AS msal FROM Employee as e) ON e.managerId = mid
WHERE e.salary > msal
