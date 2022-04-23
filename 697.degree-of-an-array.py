#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

from typing import List


# @lc code=start
# Solution 1 (Get left and right index)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 24.78 % of python3 submissions
# Your memory usage beats 57.46 % of python3 submissions (15.4 MB)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for i, n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            count[n] = count.get(n, 0) + 1

        ans = len(nums)
        degree = max(count.values())

        for n in count:
            if count[n] == degree:
                ans = min(ans, (right[n] - left[n] + 1))

        return ans

# @lc code=end
