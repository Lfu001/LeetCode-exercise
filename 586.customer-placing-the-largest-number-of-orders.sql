--
-- @lc app=leetcode id=586 lang=mysql
--
-- [586] Customer Placing the Largest Number of Orders
--

-- @lc code=start
-- Solution 1 (sort and LIMIT)
-- Your runtime beats 59.54 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    customer_number
FROM
    Orders
GROUP BY
    customer_number
ORDER BY
    COUNT(*) DESC
LIMIT
    1;

-- @lc code=end
