select seat_id from cinema c
where exists(
    select seat_id from cinema b
    where c.seat_id + 1 = b.seat_id and b.free = 1 or c.seat_id - 1 = b.seat_id and b.free = 1
) and free = 1
order by seat_id
