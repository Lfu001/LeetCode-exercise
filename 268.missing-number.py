#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
# Solution 3
# Your runtime beats 21.93 % of python3 submissions
# Your memory usage beats 87.23 % of python3 submissions (15.1 MB)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for index, num in enumerate(nums):
            ans = ans ^ index ^ num
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 18.27 % of python3 submissions
# Your memory usage beats 38.01 % of python3 submissions (15.3 MB)

# def missingNumber(self, nums: List[int]) -> int:
#     n = len(nums)
#     sum_ = n * (n + 1) // 2
#     for num in nums:
#         sum_ -= num
#     return sum_


# Solution 2
# Your runtime beats 85.17 % of python3 submissions
# Your memory usage beats 87.23 % of python3 submissions (15.2 MB)

# def missingNumber(self, nums: List[int]) -> int:
#     n = len(nums)
#     sum_ = n * (n + 1) >> 1
#     for num in nums:
#         sum_ -= num
#     return sum_
