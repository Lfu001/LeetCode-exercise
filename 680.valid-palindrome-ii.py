#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
# Solution 2 (Recursive)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 57.21 % of python3 submissions
# Your memory usage beats 91.92 % of python3 submissions (14.5 MB)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return helper(s, left, (right - 1)) or helper(s, (left + 1), right)
            left += 1
            right -= 1

        return True

# @lc code=end

# Solution 1 (Iterative: reverse string and compare when there is a mismatch)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 94.35 % of python3 submissions
# Your memory usage beats 91.92 % of python3 submissions (14.5 MB)

# def validPalindrome(self, s: str) -> bool:
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             deleteLeft = s[(left + 1):(right + 1)]
#             deleteRight = s[left:right]
#             return deleteLeft == deleteLeft[::-1] or deleteRight == deleteRight[::-1]
#         left += 1
#         right -= 1
#     return True
