#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

from typing import List


# @lc code=start
# Solution 2 (Compare with top-left neighbor)
# Time complexity: O(mn), Space complexity: O(1)
# Your runtime beats 96.81 % of python3 submissions
# Your memory usage beats 98.81 % of python3 submissions (13.7 MB)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(
            r == 0 or c == 0 or matrix[r - 1][c - 1] == val
            for r, row in enumerate(matrix)
            for c, val in enumerate(row)
        )


# @lc code=end

# Solution 1 (Compare rows: list.__eq__)
# Time complexity: O(mn), Space complexity: O(n)
# Your runtime beats 44.64 % of python3 submissions
# Your memory usage beats 37.7 % of python3 submissions (14 MB)

# def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#     return all(
#         ([matrix[i + 1][0]] + matrix[i][:-1]) == matrix[i + 1]
#         for i in range(len(matrix) - 1)
#     )
