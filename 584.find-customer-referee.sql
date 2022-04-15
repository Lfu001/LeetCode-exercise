--
-- @lc app=leetcode id=584 lang=mysql
--
-- [584] Find Customer Referee
--
-- @lc code=start
-- Solution 2 (IFNULL)
-- Your runtime beats 25.53 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    name
FROM
    Customer
WHERE
    IFNULL(referee_id, 0) <> 2;

-- @lc code=end

-- Solution 1 (<> and IS NULL)
-- Your runtime beats 46.35 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

-- SELECT
--     name
-- FROM
--     Customer
-- WHERE
--     referee_id <> 2
--     OR referee_id IS NULL;
