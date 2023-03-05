
select num from 
(
    select num, count(*) cnt from mynumbers group by num having count(*)= 1 order by num desc limit 1 
) a 
union (select null) limit 1;
