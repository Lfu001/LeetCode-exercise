--
-- @lc app=leetcode id=511 lang=mysql
--
-- [511] Game Play Analysis I
--

-- @lc code=start
-- Your runtime beats 60.47 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
SELECT
       player_id,
       MIN(event_date) as first_login
FROM
       Activity
GROUP BY
       player_id 

-- @lc code=end