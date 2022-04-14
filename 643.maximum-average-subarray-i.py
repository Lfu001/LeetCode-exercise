#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

import operator
from itertools import accumulate
from typing import List


# @lc code=start
# Solution 2 (Accumulate sums)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 5.06 % of python3 submissions (26.4 MB)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cumsum = [0] + list(accumulate(nums))
        return max(map(operator.sub, cumsum[k:], cumsum)) / k

# @lc code=end

# Solution 1 (Conv-1D) Time Limit Exceeded
# Time complexity: O(k*(n-k)), Space complexity: O(k)

# def findMaxAverage(self, nums: List[int], k: int) -> float:
#     maxSum = float("-inf")
#     for i in range(len(nums) - k + 1):
#         sumOfSubarray = sum(nums[i:(i + k)])
#         if maxSum < sumOfSubarray:
#             maxSum = sumOfSubarray
#     return maxSum / k
