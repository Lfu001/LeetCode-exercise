#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

from typing import List


# @lc code=start
# Solution 1 (Sliding window)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 67.89 % of python3 submissions
# Your memory usage beats 50.69 % of python3 submissions (15.4 MB)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = lengthOfCIS = 0
        for i in range(0, (len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                lengthOfCIS += 1
            else:
                ans = max(ans, (lengthOfCIS + 1))
                lengthOfCIS = 0
        return max(ans, (lengthOfCIS + 1))

# @lc code=end
