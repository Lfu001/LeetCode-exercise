#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# Your runtime beats 98.31 % of python3 submissions
# Your memory usage beats 43.7 % of python3 submissions (14.7 MB)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# @lc code=end

# Solution 1
# Your runtime beats 96.14 % of python3 submissions
# Your memory usage beats 43.7 % of python3 submissions (14.7 MB)

# def isPalindrome(self, s: str) -> bool:
#     s = "".join(filter(str.isalnum, s)).lower()
#     return s == s[::-1]
