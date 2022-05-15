#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

from typing import List


# @lc code=start
# Solution 3 (Built-in Timsort (in-place): list.sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 79.89 % of python3 submissions
# Your memory usage beats 61.16 % of python3 submissions (14.7 MB)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=(lambda x: x & 1))
        return nums


# @lc code=end

# Solution 1 (Swap sort (in-place))
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 24.13 % of python3 submissions
# Your memory usage beats 96.38 % of python3 submissions (14.6 MB)

# def sortArrayByParity(self, nums: List[int]) -> List[int]:
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         while left < right and not (nums[left] % 2):
#             left += 1
#         while left < right and (nums[right] % 2):
#             right -= 1
#         nums[left], nums[right] = nums[right], nums[left]
#     return nums


# Solution 2 (Built-in Timsort: sorted)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 93.26 % of python3 submissions
# Your memory usage beats 17.6 % of python3 submissions (14.7 MB)

# def sortArrayByParity(self, nums: List[int]) -> List[int]:
#     return sorted(nums, key=(lambda x: x & 1))
