#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

import bisect
from typing import List


# @lc code=start
# Solution 4 (Binary search: check if the target is the largest first)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 5.21 % of python3 submissions
# Your memory usage beats 91.34 % of python3 submissions (14.3 MB)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        return letters[bisect.bisect_right(letters, target)]


# @lc code=end

# Solution 1 (Binary search: bisect.bisect_right)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 55.35 % of python3 submissions
# Your memory usage beats 63.34 % of python3 submissions (14.4 MB)

# def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#     index = bisect.bisect_right(letters, target)
#     if index == len(letters):
#         return letters[0]
#     else:
#         return letters[index]


# Solution 2 (Linear search)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 15.08 % of python3 submissions
# Your memory usage beats 21.87 % of python3 submissions (14.4 MB)

# def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#     for c in letters:
#         if c > target:
#             return c
#     return letters[0]


# Solution 3 (Linear search: check if the target is the largest first)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 61.04 % of python3 submissions
# Your memory usage beats 63.34 % of python3 submissions (14.4 MB)

# def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#     if target >= letters[-1]:
#         return letters[0]
#
#     for c in letters:
#         if c > target:
#             return c
