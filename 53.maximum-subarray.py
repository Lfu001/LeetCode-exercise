#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_ = -10 ** 4 - 1
        for i in nums:
            s = max(s + i, i)
            max_ = max(max_, s)
        return max_

# @lc code=end

# Solution 1
# max_ = -10 ** 4 - 1
# for i in range(1, len(nums) + 1):
#     for j in range(len(nums) - i + 1):
#         sum_ = sum(nums[j:(j + i)])
#         max_ = max(sum_, max_)
# return max_
