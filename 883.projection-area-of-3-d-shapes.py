#
# @lc app=leetcode id=883 lang=python3
#
# [883] Projection Area of 3D Shapes
#

from typing import List


# @lc code=start
# Solution 1 (Sum of each plane)
# Time complexity: O(n^2), Space complexity: O(1)
# Your runtime beats 82.12 % of python3 submissions
# Your memory usage beats 93.03 % of python3 submissions (13.9 MB)
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return (
            sum(map(lambda l: sum(map(bool, l)), grid))
            + sum(map(max, grid))
            + sum(map(max, zip(*grid)))
        )


# @lc code=end
