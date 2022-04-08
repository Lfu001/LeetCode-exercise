#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

from typing import List


# @lc code=start
# Solution 3 (Hash map: single loop)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 15.09 % of python3 submissions
# Your memory usage beats 55.37 % of python3 submissions (16 MB)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxLengthOfHS = 0
        counter = dict()
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
            numOfCurrent = counter[n]
            lengthOfLowerHS = numOfCurrent + counter.get((n - 1), -numOfCurrent)
            lengthOfHigherHS = numOfCurrent + counter.get((n + 1), -numOfCurrent)
            maxLengthOfHS = max(maxLengthOfHS, lengthOfLowerHS, lengthOfHigherHS)
        return maxLengthOfHS

# @lc code=end

# Solution 1 (Sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 61.02 % of python3 submissions
# Your memory usage beats 97.72 % of python3 submissions (15.4 MB)

# def findLHS(self, nums: List[int]) -> int:
#     nums = sorted(nums)
#     prevCount = 1
#     maxLengthOfHS = 0
#     i = 0
#     while i < len(nums):
#         currCount = 1
#         t = i
#         while (i < (len(nums) - 1)) and (nums[i] == nums[i + 1]):
#             currCount += 1
#             i += 1
#         if (t > 0) and ((nums[t] - nums[t - 1]) == 1):
#             lengthOfHS = currCount + prevCount
#             maxLengthOfHS = max(maxLengthOfHS, lengthOfHS)
#         prevCount = currCount
#         i += 1
#     return maxLengthOfHS


# Solution 2 (Hash map: collections.Counter)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 54.61 % of python3 submissions
# Your memory usage beats 25.95 % of python3 submissions (16.1 MB)

# def findLHS(self, nums: List[int]) -> int:
#     maxLengthOfHS = 0
#     counter = Counter(nums)
#     for key in counter.keys():
#         if (key + 1) in counter:
#             lengthOfHS = counter[key] + counter[key + 1]
#             maxLengthOfHS = max(maxLengthOfHS, lengthOfHS)
#     return maxLengthOfHS
