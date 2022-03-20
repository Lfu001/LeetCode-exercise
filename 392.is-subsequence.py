#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
# Solution 1 (Two pointers)
# Time complexity: O(len(t)), Space complexity: O(1)
# Your runtime beats 18.88 % of python3 submissions
# Your memory usage beats 86.41 % of python3 submissions (13.8 MB)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        p = 0

        for character in s:
            while p < len(t) and character != t[p]:
                p += 1

            if p == len(t):
                return False

            p += 1

        return True

# @lc code=end
