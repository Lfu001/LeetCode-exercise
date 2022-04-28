#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

from typing import List


# @lc code=start
# Solution 2 (Get sum of nums first)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 95.09 % of python3 submissions
# Your memory usage beats 51.38 % of python3 submissions (15.3 MB)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        leftSum = 0
        for i, n in enumerate(nums):
            if leftSum == (sum_ - leftSum - n):
                return i
            leftSum += n
        return -1


# @lc code=end

# Solution 1 (Brute force): Time Limit Exceeded
# Time complexity: O(n^2), Space complexity: O(n)

# def pivotIndex(self, nums: List[int]) -> int:
#     for i in range(len(nums)):
#         if sum(nums[:i]) == sum(nums[(i + 1):]):
#             return i
#     return -1
