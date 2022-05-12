#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

from typing import List


# @lc code=start
# Solution 2 (Optimized solution 1)
# Time complexity: O(m+n), Space complexity: O(n)
# Your runtime beats 93.09 % of python3 submissions
# Your memory usage beats 45.26 % of python3 submissions (16.5 MB)
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alpha = (sum(bobSizes) - sum(aliceSizes)) // 2
        bobBoxes = set(bobSizes)
        for x in aliceSizes:
            y = x + alpha
            if y in bobBoxes:
                return [x, y]


# @lc code=end

# Solution 1 (Math)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 41.14 % of python3 submissions
# Your memory usage beats 8.47 % of python3 submissions (17.1 MB)

# def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
#     totalAlice = sum(aliceSizes)
#     totalBob = sum(bobSizes)
#     bobBoxes = set(bobSizes)
#     for x in set(aliceSizes):
#         y = x + (totalBob - totalAlice) // 2
#         if y in bobBoxes:
#             return [x, y]
