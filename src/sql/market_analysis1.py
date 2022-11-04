# Write your MySQL query statement below
select user_id buyer_id, join_date join_date, ifnull(num,0) orders_in_2019
from users u
left join (
    select buyer_id, count(*)num from orders 
        where '2019-01-01' <= order_date and order_date <= '2019-12-31'
    group by buyer_id
    ) o
on u.user_id = buyer_id 
group by user_id
