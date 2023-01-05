# Write your MySQL query statement below

select request_at as Day, round(sum(if(status = "cancelled_by_driver" or status = "cancelled_by_client", 1,0 )) / count(id) ,2) as "Cancellation Rate"
from Trips 
where client_id  not in (select users_id from Users  where banned = "Yes") 
and driver_id   not in (select users_id from Users  where banned = "Yes")
and request_at between "2013-10-01" and "2013-10-03"
group by request_at 
order by 1;
/*
select cancel.Day, round(cancel.num / total.num, 2) 'Cancellation Rate' 
from (
select count(*) num, request_at day 
from trips t
join users c
on t.client_id = c.users_id
join users d
on t.driver_id  = d.users_id
where status in ('cancelled_by_driver', 'cancelled_by_client')
and c.banned = 'No'
and d.banned = 'No'
group by request_at
) cancel
join
(
select count(*) num, request_at day 
from trips t
join users c
on t.client_id = c.users_id
join users d
on t.driver_id  = d.users_id
where
 c.banned = 'No' and d.banned = 'No'
group by request_at
) total
on cancel.day = total.day
where
total.day in ('2013-10-01', '2013-10-02', '2013-10-03');
*/
