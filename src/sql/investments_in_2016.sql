# Write your MySQL query statement below
select round(sum(i.tiv_2016), 2) tiv_2016
from insurance i
where
exists (select tiv_2015 from insurance i2 where i.tiv_2015 = i2.tiv_2015 and i.pid != i2.pid)
and
not exists (select * from insurance i2 where i2.lat = i.lat and i2.lon = i.lon and i.pid != i2.pid);
