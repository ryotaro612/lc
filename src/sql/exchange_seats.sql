with id_pair as (
    select 
    (case 
        when id % 2 = 0 then id - 1
        when id = (select max(s2.id) from seat s2) then id
        else id + 1
     end
    ) id,
    student
    from seat
)
select * from id_pair order by id;
