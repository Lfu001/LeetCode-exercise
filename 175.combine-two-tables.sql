--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--

-- @lc code=start
-- Your runtime beats 5 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
# Write your MySQL query statement below
   SELECT firstname, lastname, city, state
     FROM Person
LEFT JOIN Address
       ON Person.personID = Address.personID

-- @lc code=end

