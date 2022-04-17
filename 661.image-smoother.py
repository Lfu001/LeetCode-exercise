#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

from copy import deepcopy
from typing import List


# @lc code=start
# Solution 2 (Create return objext using copy.deepcopy)
# Time complexity: O(nm), Space complexity: O(1)
# Your runtime beats 79.4 % of python3 submissions
# Your memory usage beats 80.81 % of python3 submissions (14.7 MB)
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        width = len(img[0])
        height = len(img)
        res = deepcopy(img)
        for i in range(width):
            for j in range(height):
                neighbors = [
                    img[y][x]
                    for x in ((i - 1), i, (i + 1))
                    for y in ((j - 1), j, (j + 1))
                    if 0 <= x < width and 0 <= y < height
                ]
                res[j][i] = sum(neighbors) // len(neighbors)
        return res

# @lc code=end

# Solution 1 (Create return objext manually)
# Time complexity: O(nm), Space complexity: O(1)
# Your runtime beats 88.28 % of python3 submissions
# Your memory usage beats 97.17 % of python3 submissions (14.6 MB)

# def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#     width = len(img[0])
#     height = len(img)
#     res = [[0] * width for _ in range(height)]
#     for i in range(width):
#         for j in range(height):
#             neighbors = [
#                 img[y][x]
#                 for x in ((i - 1), i, (i + 1))
#                 for y in ((j - 1), j, (j + 1))
#                 if 0 <= x < width and 0 <= y < height
#             ]
#             res[j][i] = sum(neighbors) // len(neighbors)
#     return res
