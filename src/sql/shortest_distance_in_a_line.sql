# Write your MySQL query statement below
select min(shortest) shortest from (
select p.x - pp.x shortest
from point p
cross join point pp
) a where shortest > 0
