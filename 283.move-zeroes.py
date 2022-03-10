#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
# Solution 2 (Copy and fill)
# Your runtime beats 67.87 % of python3 submissions
# Your memory usage beats 17.09 % of python3 submissions (15.7 MB)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = 0
        zeroPointer = 0

        while p < len(nums):
            if nums[p] != 0:
                nums[zeroPointer] = nums[p]
                zeroPointer += 1
            p += 1

        while zeroPointer < len(nums):
            nums[zeroPointer] = 0
            zeroPointer += 1

# @lc code=end

# Solution 1 (Swap)
# Your runtime beats 49.42 % of python3 submissions
# Your memory usage beats 52.86 % of python3 submissions (15.5 MB)

# def moveZeroes(self, nums: List[int]) -> None:
#     p = 0
#     zeroPointer = 0
#
#     while p < len(nums):
#         if nums[p] != 0:
#             tmp = nums[p]
#             nums[p] = nums[zeroPointer]
#             nums[zeroPointer] = tmp
#             zeroPointer += 1
#         p += 1
