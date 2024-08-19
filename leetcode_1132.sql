# Write your MySQL query statement below
-- 1132. Reported Posts II
-- Actions tend to be ENUMs
-- Think about query decomposition for complex SQL query logic
-- 20 minutes but solutioned today at least : you got it!!!
WITH SPAM_DAYS AS (
    SELECT DISTINCT A.action_date
    FROM Actions AS A
    WHERE A.action = "report" AND A.extra= "spam"
    ORDER BY A.action_date ASC
), REPORTED_POSTS_PER_DATE AS (
    SELECT DISTINCT A.action_date, A.post_id
    FROM Actions AS A
    WHERE A.action = "report" AND A.action = "report" AND a.extra = "spam"
    ORDER BY A.action_date ASC, A.post_id ASC
), REMOVED_SPAM_POSTS AS(
    SELECT DISTINCT A.action_date, A.post_id
    FROM Actions AS A
    INNER JOIN Removals AS R
    ON A.post_id = R.post_id
    WHERE A.action = "report" AND A.extra = "spam"
    ORDER BY A.action_date, A.post_id
), REPORTED_REMOVED AS (
    SELECT DISTINCT A.action_date, A.post_id, S.post_id AS `other`
    FROM REPORTED_POSTS_PER_DATE AS A
    LEFT JOIN REMOVED_SPAM_POSTS AS S
    ON A.post_id = S.post_id
), FINAL_REPORT AS (
    SELECT A.action_date,
    SUM(CASE WHEN A.post_id = A.other THEN 1 ELSE 0 END) / COUNT(*) AS `daily_percent`
    FROM REPORTED_REMOVED AS A
    GROUP BY A.action_date
), RESULT AS (
    SELECT ROUND(100*(AVG(daily_percent)),2) AS `average_daily_percent` FROM FINAL_REPORT
) SELECT * FROM RESULT
    
