# Write your MySQL query statement below
with many as (
  select *
  from stadium
  where people >= 100
)
select * from many m
where
  exists (select * from many m2 where m2.id = m.id + 1)
  and
  exists (select * from many m2 where m2.id = m.id + 2)
  or
  exists (select * from many m2 where m2.id = m.id - 1)
  and
  exists (select * from many m2 where m2.id = m.id + 1)
  or
  exists (select * from many m2 where m2.id = m.id - 2)
  and
  exists (select * from many m2 where m2.id = m.id - 1)
order by
visit_date
