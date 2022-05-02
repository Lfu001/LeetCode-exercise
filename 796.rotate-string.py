#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
# Solution 1 (Construct larger string)
# Time complexity: O(n), Space complexity: O(len(s))
# Your runtime beats 99.84 % of python3 submissions
# Your memory usage beats 14.93 % of python3 submissions (13.9 MB)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s * 2)


# @lc code=end
