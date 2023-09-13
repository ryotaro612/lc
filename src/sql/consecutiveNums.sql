# Write your MySQL query statement below
select distinct l.num ConsecutiveNums from logs l join logs l2 on l.id + 1 = l2.id and l.num = l2.num join logs l3 on l2.id + 1 = l3.id and l2.num = l3.num; 
