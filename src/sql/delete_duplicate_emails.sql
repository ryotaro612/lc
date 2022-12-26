# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

delete from person where id not in (
    select a.id from (select min(id) id from person group by email) a
);
