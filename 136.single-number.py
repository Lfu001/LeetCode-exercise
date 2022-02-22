#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# Your runtime beats 45.57 % of python3 submissions
# Your memory usage beats 75.94 % of python3 submissions (16.6 MB)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 56.56 % of python3 submissions
# Your memory usage beats 40.32 % of python3 submissions (16.7 MB)

# def singleNumber(self, nums: List[int]) -> int:
#     counter = dict()
#     for n in nums:
#         if n in counter:
#             counter[n] += 1
#         else:
#             counter[n] = 0
#     return next(key for key, val in counter.items() if val == 0)
