# Write your MySQL query statement below
/*
-- Syntax to add 5 days to September 1, 2011 (input date) the function would be
DATEADD(DAY, 5, '9/1/2011')

-- Syntax to subtract 5 months from September 1, 2011 (input date) the function would be
DATEADD(MONTH, -5, '9/1/2011')
*/
select distinct Id
from weather w
left join (
    select date_add(recordDate, interval 1 day) yesterday, temperature
    from weather
) j
on w.recordDate = j.yesterday
where
 w.temperature > j.temperature;
