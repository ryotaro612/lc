select
    round(
        ifnull(
            (select count(*) from (select distinct requester_id, accepter_id from RequestAccepted) b)
            /
            (select count(*) from (select distinct sender_id, send_to_id from FriendRequest) a)
            ,
        0)
    ,
    2) accept_rate;
