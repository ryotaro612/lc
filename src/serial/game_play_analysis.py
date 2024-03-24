# Write your MySQL query statement below
with 
second_login_date as (
  select player_id,  date_add(min(event_date), interval 1 day) event_date
  from activity
  group by player_id
),
num_of_second_login_users as (
    select count(*) num
    from activity a
    join second_login_date s
    on a.player_id = s.player_id and a.event_date = s.event_date
),
num_of_users as (
    select count(distinct player_id) unique_users
    from activity
)
select round(
    (select num from num_of_second_login_users)/ (select unique_users from num_of_users),
    2
) fraction;
