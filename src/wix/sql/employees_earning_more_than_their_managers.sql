# Write your MySQL query statement below
select a.name Employee
from employee a
join employee b
on a.managerId = b.id
where
a.salary > b.salary
