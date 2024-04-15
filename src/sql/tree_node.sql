# Write your MySQL query statement below
with leaf as (
    select distinct t1.id, 'Leaf' type
    from tree t1
    left join tree t2
    on t1.id = t2.p_id
    where 
    t2.p_id is null 
    and t1.p_id is not null
),
root as (
    select id, 'Root' type
    from tree
    where
    p_id is null
),
inr as (
    select distinct t1.id, 'Inner' type
    from tree t1
    join tree t2
    on t1.id = t2.p_id
    where
    t1.p_id is not null
)
select *
from leaf
union
select *
from root
union
select *
from inr;
