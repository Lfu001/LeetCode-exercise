#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

from typing import List


# @lc code=start
# Solution 1 (Get first max and second max)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 5.17 % of python3 submissions
# Your memory usage beats 13.25 % of python3 submissions (13.9 MB)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max2 = (-1, -1)
        for i, n in enumerate(nums):
            if n > max2[1]:
                if n > max1[1]:
                    max2 = max1
                    max1 = (i, n)
                else:
                    max2 = (i, n)
        return max1[0] if max1[1] >= max2[1] * 2 else -1


# @lc code=end
