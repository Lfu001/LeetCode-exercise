#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
# Your runtime beats 50.94 % of python3 submissions
# Your memory usage beats 61.79 % of python3 submissions (27.3 MB)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

# @lc code=end

# Solution 1 (Time Limit Exceeded)
# def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#     for i in range(len(nums)):
#         searchableLength = len(nums) - 1 - i
#         if searchableLength < k:
#             k = searchableLength
#         for j in range(1, (k + 1)):
#             if nums[i] == nums[i + j]:
#                 return True
#     return False
