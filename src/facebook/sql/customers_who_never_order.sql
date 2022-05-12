# Write your MySQL query statement below
select name Customers from customers c left join orders o on c.id = o.customerid where o.id is null;
