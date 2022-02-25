--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--

-- @lc code=start
-- Your runtime beats 21.04 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

# Write your MySQL query statement below
DELETE p1
  FROM Person AS p1, Person AS P2
 WHERE p1.email = p2.email AND p1.id > p2.id

-- @lc code=end
