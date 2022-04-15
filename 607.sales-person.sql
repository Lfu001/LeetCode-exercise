--
-- @lc app=leetcode id=607 lang=mysql
--
-- [607] Sales Person
--

-- @lc code=start
-- Solution 1 (GROUP BY and HAVING)
-- Your runtime beats 82.97 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    S.name
FROM
    SalesPerson AS S
    LEFT JOIN Orders AS O ON S.sales_id = O.sales_id
    LEFT JOIN Company AS C ON O.com_id = C.com_id
GROUP BY
    S.name
HAVING
    COUNT(order_id) = 0
    OR NOT SUM(C.name = "RED") > 0;

-- @lc code=end
