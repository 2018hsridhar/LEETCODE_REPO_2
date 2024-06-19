# Write your MySQL query statement below
-- Solve for cancellation rate
-- gaaah unknown col field list
-- interpretation as a column
-- 30 minutes
WITH NBU AS (
    SELECT users_id FROM USERS
    WHERE banned = 'No'
),
-- SELECT * FROM NONBANNEDUSERS
VALID_TRIPS AS (
    SELECT * FROM Trips AS T
    WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03' AND T.client_id IN(select users_id FROM NBU) AND T.driver_id IN(select users_id FROM NBU)
), ANALYTICS AS (
    SELECT *,
        SUM(1) AS numTrips,
            SUM(
            CASE 
            WHEN status = "cancelled_by_driver" OR status = "cancelled_by_client"
            THEN 1 
            ELSE 0 
            END) as numCancelledTrips
    FROM VALID_TRIPS
    GROUP BY request_at
    ORDER BY request_at ASC
) SELECT request_at as 'Day', ROUND((numCancelledTrips / numTrips), 2) as 'Cancellation Rate' FROM ANALYTICS

