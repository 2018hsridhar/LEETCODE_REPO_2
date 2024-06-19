-- 185. Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/
# Write your MySQL query statement below
-- Commit Log :
-- FK as a reference column ( to another tables )
-- Get top three unique salaries ( for each department )
-- Then get the employees per department with said salaries
-- May need CTEs
-- create sets to search a WHERE on later

-- WITH uniqueSalariesPerDepartment AS(
--     SELECT DISTINCT salary FROM Employee
--     GROUP BY departmentId
-- )
-- For each departmentId, can we get the salary and the employee
-- the salaries should be unique ( but at the department level ) ( not across all )
-- if we have uniqueSalariesPerDepartment ... can we solution the rest?
WITH departmentSalaryRank 
AS (
        SELECT departmentId, salary, 
        row_number() OVER(
            PARTITION BY departmentId ORDER BY salary DESC
        ) AS row_num
    FROM Employee
    GROUP BY departmentId, salary
), topThreeSalaryPerDept AS (
    SELECT S.DepartmentId as DeptId, D.name as Department, S.Salary as Salary from departmentSalaryRank as S
    INNER JOIN Department AS D
    WHERE S.departmentId = D.id
    AND S.row_num <= 3
) 
SELECT T.Department, E.name AS Employee, T.Salary FROM Employee AS E
JOIN topThreeSalaryPerDept as T
WHERE E.departmentId = T.DeptId
AND E.salary = T.Salary

