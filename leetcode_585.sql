-- 585. Investments in 2016
-- URL := https://leetcode.com/problems/investments-in-2016/
# Write your MySQL query statement below
-- tiv_2015 : remove unique ones
-- (lat,long) : ensure uniqueness preserved ( for two columns )
-- then write up aggregation ( to two decimals )

-- select only those with unique lat,long -> group by removal needed too!
-- GROUP BY COUNT(*) pattern here :-)
-- gaaah 30 minutes on this too :-(
-- we need subquerying to support this problem
-- GROUP BY(...) and HAVING COUNT(...) lends tremendous power
-- ensure to work with original tables ( not modified CTEs ) 
WITH CTE1 AS (
    SELECT pid,tiv_2015,tiv_2016, lat, lon FROM Insurance
    GROUP BY lat,lon
    HAVING COUNT(*) = 1
), CTE2 AS (
    SELECT tiv_2015 FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) > 1
)
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016 FROM CTE1
JOIN CTE2
ON CTE1.tiv_2015 = CTE2.tiv_2015

