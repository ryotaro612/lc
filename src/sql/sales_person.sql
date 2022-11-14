select s.name
from salesperson s
where not exists
(
    select 1
    from orders o
    join company c
    on o.com_id = c.com_id
    where
    c.name = 'RED' and s.sales_id = o.sales_id
)
