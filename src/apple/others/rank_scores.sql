# Write your MySQL query statement below
select 
    score, 
    (select count(*) from 
     (select distinct score from Scores) s where s.score > a.score) + 1 as `rank`
from Scores a order by `rank`; 
