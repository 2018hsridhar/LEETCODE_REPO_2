# Write your MySQL query statement below
-- Seperate this problem into two seperate subqueries ( per bullet point )
-- 1341. Movie Rating
-- SELECT B.title FROM Movies as A JOIN MovieRating as B
-- WHERE A.

-- movie rating ( highest average rating ) in Feburyar 2020
-- Gotta learn to debug CTEs
-- Super carefu
WITH CTE1 AS 
(
    SELECT U.name, COUNT(R.user_id) AS countUserMovies FROM MovieRating as R
    JOIN Users as U
    ON R.user_id = U.user_id
    GROUP BY R.user_id
    ORDER BY countUserMovies DESC, U.name ASC
    LIMIT 1
),
CTE2 AS
(
    SELECT B.title, AVG(A.rating) AS avgRate FROM MovieRating as A
    JOIN Movies as B
    ON A.movie_id = B.movie_id
    WHERE YEAR(A.created_at) = 2020
    AND MONTH(A.created_at) = 2
    GROUP BY B.title
    ORDER BY avgRate DESC, B.title ASC
    LIMIT 1
)
SELECT CTE1.name as "results" FROM CTE1
UNION ALL
SELECT CTE2.title FROM CTE2
-- SELECT * FROM CTE1

