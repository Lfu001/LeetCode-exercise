#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

from typing import List


# @lc code=start
# Solution 1 (Add and subtract)
# Time complexity: O(n^2), Space complexity: O(1)
# Your runtime beats 97.52 % of python3 submissions
# Your memory usage beats 22.77 % of python3 submissions (14.1 MB)
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                currentTower = grid[i][j]
                if currentTower:
                    area += currentTower * 4 + 2
                if i:
                    area -= min(grid[i - 1][j], currentTower) * 2
                if j:
                    area -= min(grid[i][j - 1], currentTower) * 2
        return area


# @lc code=end
