#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

from math import prod
from typing import List


# @lc code=start
# Solution 4 (One-liner)
# Time complexity: O(len(ops)), Space complexity: O(len(ops))
# Your runtime beats 78.85 % of python3 submissions
# Your memory usage beats 5.74 % of python3 submissions (16.3 MB)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return prod(map(min, zip(*ops))) if ops else (m * n)

# @lc code=end

# Solution 1 (Time Limit Exceeded)
# Time complexity: O(n*m*len(ops)), Space complexity: O(nm)
# def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
#     matrix = [([0] * m) for _ in range(n)]
#     for operation in ops:
#         for i in range(operation[0]):
#             for j in range(operation[1]):
#                 matrix[i][j] += 1
#     return sum(matrix, start=[]).count(matrix[0][0])


# Solution 2 (Time Limit Exceeded)
# Time complexity: O(n*m*len(ops)), Space complexity: O(nm)
# def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
#     if not ops:
#         return m * n
#     counter = Counter()
#     for operation in ops:
#         for i in range(operation[0]):
#             for j in range(operation[1]):
#                 counter[(i, j)] += 1
#     return list(counter.values()).count(counter[(0, 0)])


# Solution 3 (Traverse ops once)
# Time complexity: O(len(ops)), Space complexity: O(1)
# Your runtime beats 41.24 % of python3 submissions
# Your memory usage beats 34.74 % of python3 submissions (16 MB)

# def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
#     min_m = m
#     min_n = n
#     for a, b in ops:
#         min_m = min(min_m, a)
#         min_n = min(min_n, b)
#     return min_m * min_n
