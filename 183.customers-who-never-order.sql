--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
-- Your runtime beats 56.24 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
# Write your MySQL query statement below
   SELECT C.name AS Customers
     FROM Customers AS C
LEFT JOIN Orders AS O
       ON C.id = O.customerId
    WHERE O.customerId IS NULL

-- @lc code=end
