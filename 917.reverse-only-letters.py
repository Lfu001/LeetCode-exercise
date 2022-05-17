#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

import re


# @lc code=start
# Solution 2 (Regex)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 34.1 % of python3 submissions
# Your memory usage beats 66.52 % of python3 submissions (13.8 MB)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        return re.sub(r"[A-Za-z]", "{}", s).format(*[c for c in s[::-1] if c.isalpha()])


# @lc code=end

# Solution 1 (Two pointers)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 17.9 % of python3 submissions
# Your memory usage beats 66.52 % of python3 submissions (13.8 MB)

# def reverseOnlyLetters(self, s: str) -> str:
#     s_list = list(s)
#     left = 0
#     right = len(s_list) - 1
#     while left < right:
#         while left < right and not s_list[left].isalpha():
#             left += 1
#         while left < right and not s_list[right].isalpha():
#             right -= 1
#         s_list[left], s_list[right] = s_list[right], s_list[left]
#         left += 1
#         right -= 1
#     return "".join(s_list)
