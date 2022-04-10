--
-- @lc app=leetcode id=595 lang=mysql
--
-- [595] Big Countries
--
-- @lc code=start
-- Your runtime beats 69.1 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
(
    select
        name,
        population,
        area
    FROM
        World
    WHERE
        area >= 3000000
)
UNION
(
    select
        name,
        population,
        area
    FROM
        World
    WHERE
        population >= 25000000
);

-- @lc code=end
-- Your runtime beats 41.36 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- SELECT
--     name,
--     population,
--     area
-- FROM
--     World
-- WHERE
--     area >= 3000000
--     OR population >= 25000000