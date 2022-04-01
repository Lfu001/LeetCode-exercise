#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I
#

# @lc code=start
# Solution 1
# Time complexity: O(min(len(a),len(b))), Space complexity: O(1)
# Your runtime beats 83.68 % of python3 submissions
# Your memory usage beats 62.36 % of python3 submissions (13.9 MB)
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

# @lc code=end
