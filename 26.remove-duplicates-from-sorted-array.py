#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
            if nums[p] != nums[i]:
                p += 1
                nums[p] = nums[i]
        return p + 1


# @lc code=end

# Solution 1
# i = 0
# j = 1
# count = 0

# while j < len(nums):
#     if nums[i] == nums[j]:
#         del nums[j]
#         count += 1
#     else:
#         i += 1
#         j += 1

# k = len(nums)

# for _ in range(count):
#     nums.append(None)

# return k