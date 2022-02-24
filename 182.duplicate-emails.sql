--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--

-- @lc code=start
-- Your runtime beats 5.01 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
# Write your MySQL query statement below
  SELECT email AS Email
    FROM Person
GROUP BY email
  HAVING COUNT(email) > 1

-- @lc code=end
