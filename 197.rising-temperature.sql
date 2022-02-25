--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
-- Your runtime beats 81.47 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

# Write your MySQL query statement below
SELECT w1.id
FROM Weather AS w1, Weather AS w2
WHERE SUBDATE(w1.recordDate, 1) = w2.recordDate AND w1.temperature > w2.temperature

-- @lc code=end
