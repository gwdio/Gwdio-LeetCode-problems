select name as Customers
from Customers as c
where c.id not in (select customerId from Orders)