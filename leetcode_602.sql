# Write your MySQL query statement below
-- Need to execute a SUMMATION on two columns (in a future JOIN op )?
-- Both ids are primary keys : can we leverage this?
-- 602. Friend Requests II: Who Has the Most Friends
-- URL = https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- 10 minutes woah!
WITH DOUBLEDIR AS
(
    SELECT requester_id AS srcId, accepter_id AS dstId FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS srcId, requester_id AS dstId FROM RequestAccepted
)
SELECT srcId as id, COUNT(*) AS num FROM DOUBLEDIR
GROUP BY srcId
ORDER BY num DESC
LIMIT 1
