#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

import bisect
from typing import List


# @lc code=start
# Solution 3 (Built-in: bisect.bisect_left)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 87.89 % of python3 submissions
# Your memory usage beats 75.06 % of python3 submissions (15.4 MB)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


# @lc code=end

# Solution 1 (Iterative)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 30.97 % of python3 submissions
# Your memory usage beats 23.94 % of python3 submissions (15.6 MB)

# def search(self, nums: List[int], target: int) -> int:
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         else:
#             return mid
#     return -1


# Solution 2 (Recursive)
# Time complexity: O(logn), Space complexity: O(logn)
# Your runtime beats 98.39 % of python3 submissions
# Your memory usage beats 23.94 % of python3 submissions (22.7 MB)

# def search(self, nums: List[int], target: int) -> int:
#     def binarySearch(left: int, right: int) -> int:
#         if left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 return mid
#             return binarySearch(left, right)
#         else:
#             return -1
#
#     return binarySearch(0, (len(nums) - 1))
