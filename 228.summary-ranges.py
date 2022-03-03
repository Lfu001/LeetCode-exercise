#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
# Your runtime beats 99.95 % of python3 submissions
# Your memory usage beats 78.05 % of python3 submissions (13.9 MB)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        current = 0
        while current < len(nums):
            start = nums[current]
            while current < (len(nums) - 1) and nums[current + 1] - nums[current] == 1:
                current += 1
            if nums[current] == start:
                ans.append(str(start))
            else:
                ans.append("{}->{}".format(start, nums[current]))
            current += 1
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 28.1 % of python3 submissions
# Your memory usage beats 30.8 % of python3 submissions (13.9 MB)

# def summaryRanges(self, nums: List[int]) -> List[str]:
#     if not nums:
#         return nums
#     elif len(nums) == 1:
#         return [str(nums[0])]
#     else:
#         ans = []
#         start = end = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i - 1] != 1:
#                 if nums[i - 1] == start:
#                     ans.append(str(start))
#                 else:
#                     end = nums[i - 1]
#                     ans.append("{}->{}".format(start, end))
#                 start = end = nums[i]
#         if end == nums[-1]:
#             ans.append(str(end))
#         else:
#             end = nums[-1]
#             ans.append("{}->{}".format(start, end))
#         return ans
