select user_id id , sum(num) num (
select * from (
    select requester_id user_id, count(*) num from requestAccepted group by requester_id
) a
union all
select accepter_id user_id, count(*) num from requestAccepted group by accepter_id
    ) x
group by id
;
