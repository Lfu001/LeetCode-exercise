#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

from typing import List


# @lc code=start
# Solution 2 (Reversed iterator)
# Time complexity: O(n^2), Space complexity: O(1)
# Your runtime beats 70.34 % of python3 submissions
# Your memory usage beats 97.74 % of python3 submissions (13.7 MB)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[i ^ 1 for i in reversed(row)] for row in image]


# @lc code=end

# Solution 1 (Two pointers: in-place)
# Time complexity: O(n^2), Space complexity: O(1)
# Your runtime beats 96.41 % of python3 submissions
# Your memory usage beats 20.8 % of python3 submissions (13.9 MB)

# def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#     for row in image:
#         left = 0
#         right = len(row) - 1
#         for _ in range(len(row) // 2):
#             row[left], row[right] = row[right], row[left]
#             left += 1
#             right -= 1
#         row[:] = map(partial(operator.xor, 1), row)
#     return image
