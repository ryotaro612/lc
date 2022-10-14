# Write your MySQL query statement below
select email Email from(
    
select count(*) num, email
from person group by email
having num > 1
) a;
