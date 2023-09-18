# Write your MySQL query statement below
select d.department Department, e.name Employee, e.salary Salary
from employee e
join (
select max(e.salary) max_salary, d.name Department, departmentId
    from employee e
    join department d
    on e.departmentId = d.id
    group by e.departmentId
) d
on d.max_salary = e.salary and d.departmentId = e.departmentId
;

/*
select d.name Department, e.name Employee, e.salary Salary 
from employee e 
join (
    select distinct e.id
    from employee e
    join department d
    on e.departmentId = d.id
    group by e.departmentId
    having e.salary = max(e.salary)
) on e.departmentId = d.id
group 
*/
