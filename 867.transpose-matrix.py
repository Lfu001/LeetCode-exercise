#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

from typing import List


# @lc code=start
# Solution 2 (Simplify solution 1)
# Time complexity: O(mn), Space complexity: O(1)
# Your runtime beats 43.05 % of python3 submissions
# Your memory usage beats 92.46 % of python3 submissions (14.6 MB)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))


# @lc code=end

# Solution 1 (Zip)
# Time complexity: O(mn), Space complexity: O(1)
# Your runtime beats 63.79 % of python3 submissions
# Your memory usage beats 16.5 % of python3 submissions (14.9 MB)

# def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#     return [list(col) for col in zip(*matrix)]
