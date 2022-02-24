--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
-- Your runtime beats 28.13 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
# Write your MySQL query statement below
SELECT A.name AS Employee
  FROM Employee AS A
  JOIN Employee AS B
    ON A.managerId = B.id
   AND A.salary > B.salary

-- @lc code=end

-- Solution 1
-- Your runtime beats 42.2 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- # Write your MySQL query statement below
--    SELECT A.name AS Employee
--      FROM Employee AS A
-- LEFT JOIN Employee AS B
--        ON A.managerId = B.id
--     WHERE A.salary > B.salary
