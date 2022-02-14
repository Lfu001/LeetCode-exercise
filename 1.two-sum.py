#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = dict()
        for i in range(len(nums)):
            x = (target - nums[i])
            if x in numToIndex:
                return [numToIndex[x], i]
            numToIndex[nums[i]] = i

# @lc code=end

# Solution 1
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             return [i, j]

# Solution 2
# numToIndex = dict()
# for i in range(len(nums)):
#     numToIndex[nums[i]] = i
# for i in range(len(nums)):
#     x = target - nums[i]
#     if x in numToIndex and numToIndex[x] != i:
#         return [i, numToIndex[x]]
