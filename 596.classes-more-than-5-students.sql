--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--
-- @lc code=start
-- Your runtime beats 12.51 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    class
FROM
    Courses
GROUP BY
    class
HAVING
    COUNT(class) >= 5;

-- @lc code=end