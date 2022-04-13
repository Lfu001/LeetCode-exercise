--
-- @lc app=leetcode id=627 lang=mysql
--
-- [627] Swap Salary
--
-- @lc code=start
-- Your runtime beats 21.41 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
UPDATE
    Salary
SET
    sex = REPLACE("fm", sex, "");

-- @lc code=end

-- Solution 1 (CASE)
-- Your runtime beats 5.03 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

-- UPDATE
--     Salary
-- SET
--     sex = CASE
--         sex
--         WHEN "m" THEN "f"
--         ELSE "m"
--     END;


-- Solution 2(IF)
-- Your runtime beats 23.66 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

-- UPDATE
--     Salary
-- SET
--     sex = IF (sex = "m", "f", "m");
