--
-- @lc app=leetcode id=620 lang=mysql
--
-- [620] Not Boring Movies
--
-- @lc code=start
-- Solution 2 (MOD())
-- Your runtime beats 25.57 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    *
FROM
    Cinema
WHERE
    MOD(id, 2) = 1
    AND NOT description = "boring"
ORDER BY
    rating DESC;

-- @lc code=end

-- Solution 1 (% operator)
-- Your runtime beats 68.77 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
    id,
    movie,
    description,
    rating
FROM
    Cinema
WHERE
    id % 2 = 1
    AND NOT description = "boring"
ORDER BY
    rating DESC;