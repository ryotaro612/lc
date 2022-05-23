# Write your MySQL query statement below

select
  d.name Department, a.name Employee, a.Salary
from (
    select 
        name, 
        salary, 
        dense_rank() over (partition by departmentid order by salary desc) ranking, 
    departmentid
    from employee
) a
join department d
on a.departmentid = d.id
where
  a.ranking <= 3
;

/*
{"headers": ["name", "salary", "rank", "departmentid"], "values": 
[["Max", 90000, 1, 1], 
["Joe", 85000, 2, 1], 
["Randy", 85000, 2, 1], 
["Will", 70000, 3, 1], 
["Janet", 69000, 4, 1], 
["Henry", 80000, 1, 2], 
["Sam", 60000, 2, 2]]}

{"headers": ["Department", "Employee", "Salary"], "values": 
[["IT", "Max", 90000], 
["IT", "Joe", 85000], 
["IT", "Randy", 85000], 
["IT", "Will", 70000], 
["Sales", "Henry", 80000], 
["Sales", "Sam", 60000]]}

*/
