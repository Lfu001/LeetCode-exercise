#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
# Your runtime beats 23.92 % of python3 submissions
# Your memory usage beats 68.04 % of python3 submissions (13.9 MB)
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

# @lc code=end

# (1)  o 1 -> 0
# (2)  o 2 -> 0
# (3)  o 3 -> 0

# (4)  x 4 -> 1 -> (1)
# (5)  x 4 -> 2 -> (2)
# (6)  x 4 -> 3 -> (3)

# (7)  o 5 -> 4 -> (4)-(6)

# (8)  o 6 -> 4 -> (4)-(6)

# (9)  o 7 -> 4 -> (4)-(6)

# (10) x 8 -> 5 -> (7)
# (11) x 8 -> 6 -> (8)
# (12) x 8 -> 7 -> (9)
