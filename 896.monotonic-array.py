#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

from typing import List


# @lc code=start
# Solution 3 (One pass: without shortcut)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 84.81 % of python3 submissions (28 MB)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            elif nums[i] < nums[i + 1]:
                decreasing = False
        return increasing or decreasing


# @lc code=end

# Solution 1 (Straightforward)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 56.97 % of python3 submissions
# Your memory usage beats 11.71 % of python3 submissions (28.6 MB)

# def isMonotonic(self, nums: List[int]) -> bool:
#     return any(all(map(op, nums, nums[1:])) for op in (operator.le, operator.ge))


# Solution 2 (One pass: with shortcut)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 48.61 % of python3 submissions
# Your memory usage beats 84.81 % of python3 submissions (28 MB)

# def isMonotonic(self, nums: List[int]) -> bool:
#     increasing = decreasing = True
#     for i in range(len(nums) - 1):
#         if increasing and nums[i] > nums[i + 1]:
#             increasing = False
#             if not decreasing:
#                 break
#         elif decreasing and nums[i] < nums[i + 1]:
#             decreasing = False
#             if not increasing:
#                 break
#     return increasing or decreasing
