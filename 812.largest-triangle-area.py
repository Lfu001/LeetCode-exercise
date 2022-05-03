#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

from itertools import combinations
from typing import List

# @lc code=start
# # Solution 1 (Brute force: Heron's formula)
# Time complexity: O(n^3), Space complexity: O(1)
# Your runtime beats 13.82 % of python3 submissions
# Your memory usage beats 31.58 % of python3 submissions (14 MB)


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largestArea = 0
        for threePoints in combinations(points, 3):
            edgesSquared = [
                ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                for p1, p2 in combinations(threePoints, 2)
            ]
            area = (
                (4 * edgesSquared[1] * edgesSquared[2])
                - (edgesSquared[0] - edgesSquared[1] - edgesSquared[2]) ** 2
            ) ** 0.5 / 4
            if area > largestArea:
                largestArea = area
        return largestArea


# @lc code=end
