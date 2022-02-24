#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
# Your runtime beats 16.37 % of python3 submissions
# Your memory usage beats 70.02 % of python3 submissions (13.9 MB)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans *= 26
            ans += ord(c) - ord("A") + 1
        return ans

# @lc code=end
