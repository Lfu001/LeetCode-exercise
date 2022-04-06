#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

from typing import List

# @lc code=start
import numpy as np


# Solution 5 (NumPy)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 25.42 % of python3 submissions
# Your memory usage beats 6.15 % of python3 submissions (32.4 MB)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            return np.reshape(mat, (r, c))
        except ValueError:
            return mat

# @lc code=end

# Solution 1 (Merge and split: append one by one)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 26.14 % of python3 submissions
# Your memory usage beats 13.8 % of python3 submissions (14.8 MB)

# def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#     if (len(mat) * len(mat[0])) != (r * c):
#         return mat
#
#     elements = sum(mat, start=[])
#     reshapedMatrix = []
#     i = 0
#
#     while i < len(elements):
#         reshapedRow = []
#         while len(reshapedRow) < c:
#             reshapedRow.append(elements[i])
#             i += 1
#         reshapedMatrix.append(reshapedRow)
#
#     return reshapedMatrix


# Solution 2 (Merge and split: generator)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 20.92 % of python3 submissions
# Your memory usage beats 39.74 % of python3 submissions (14.7 MB)

# def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#     if (len(mat) * len(mat[0])) != (r * c):
#         return mat
#
#     def generate_batch(seq, batchSize):
#         for i in range(0, len(seq), batchSize):
#             yield seq[i:(i + batchSize)]
#
#     return [row for row in generate_batch(sum(mat, start=[]), c)]


# Solution 3 (Traverse once)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 33.67 % of python3 submissions
# Your memory usage beats 84.32 % of python3 submissions (14.7 MB)

# def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#     n = len(mat)
#     m = len(mat[0])
#     if (n * m) != (r * c):
#         return mat
#
#     reshapedMatrix = [[] for _ in range(r)]
#
#     for i in range(r * c):
#         reshapedMatrix[i // c].append(mat[i // m][i % m])
#
#     return reshapedMatrix


# Solution 4 (Built-in function: itertools)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 82.61 % of python3 submissions
# Your memory usage beats 84.32 % of python3 submissions (14.7 MB)

# def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#     if (len(mat) * len(mat[0])) != (r * c):
#         return mat
#     it = itertools.chain.from_iterable(mat)
#     return [list(itertools.islice(it, c)) for _ in range(r)]
