#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            if target < nums[left]:
                return left
            if target > nums[right]:
                return right + 1

            center = (left + right) // 2

            if target < nums[center]:
                right = center - 1
            elif target > nums[center]:
                left = center + 1
            else:
                return center

# @lc code=end

# Solution 1
# left = 0
# right = last = len(nums) - 1
# while True:
#     if target < nums[left]:
#         return left
#     if target > nums[right]:
#         return right + 1

#     center = (left + right) // 2

#     if target < nums[center]:
#         if left == right or center == 0:
#             return center
#         right = center - 1
#     elif target > nums[center]:
#         if left == right or center == last:
#             return center + 1
#         left = center + 1
#     else:
#         return center