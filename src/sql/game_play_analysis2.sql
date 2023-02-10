# Write your MySQL query statement below

select distinct a.player_id, device_id 
from activity a
join (
  select player_id, min(event_date) event_date from activity group by player_id
) b
on a.player_id = b.player_id and a.event_date = b.event_date;
