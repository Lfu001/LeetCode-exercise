#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

from typing import List


# @lc code=start
# Solution 4 (Count the number of continuous zeros)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 79.18 % of python3 submissions
# Your memory usage beats 33.66 % of python3 submissions (14.4 MB)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        availablePlots = 0
        zeros = 1
        for plot in flowerbed:
            if plot == 0:
                zeros += 1
            else:
                availablePlots += (zeros - 1) // 2
                zeros = 0
        return (availablePlots + (zeros // 2)) >= n

# @lc code=end

# Solution 1 (Traverse once)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 9.09 % of python3 submissions
# Your memory usage beats 78.44 % of python3 submissions (14.4 MB)

# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     availablePlots = 0
#     for i in range(len(flowerbed)):
#         if flowerbed[i] == 0:
#             emptyLeftPlot = (i == 0) or (flowerbed[i - 1] == 0)
#             emptyRightPlot = (i == (len(flowerbed) - 1)) or (flowerbed[i + 1] == 0)
#             if emptyLeftPlot and emptyRightPlot:
#                 availablePlots += 1
#                 flowerbed[i] = 1
#     return availablePlots >= n


# Solution 2 (Traverse once: optimized)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 85.5 % of python3 submissions
# Your memory usage beats 33.66 % of python3 submissions (14.5 MB)

# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     availablePlots = 0
#     for i in range(len(flowerbed)):
#         if flowerbed[i] == 0:
#             emptyLeftPlot = (i == 0) or (flowerbed[i - 1] == 0)
#             emptyRightPlot = (i == (len(flowerbed) - 1)) or (flowerbed[i + 1] == 0)
#             if emptyLeftPlot and emptyRightPlot:
#                 availablePlots += 1
#                 flowerbed[i] = 1
#                 if availablePlots >= n:
#                     return True
#     return availablePlots >= n


# Solution 3 (Dummy)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 47.14 % of python3 submissions
# Your memory usage beats 33.66 % of python3 submissions (14.4 MB)

# def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#     availablePlots = 0
#     flowerbed = [0] + flowerbed + [0]
#     for i in range(1, (len(flowerbed) - 1)):
#         if flowerbed[i] == 0:
#             emptyLeftPlot = (flowerbed[i - 1] == 0)
#             emptyRightPlot = (flowerbed[i + 1] == 0)
#             if emptyLeftPlot and emptyRightPlot:
#                 availablePlots += 1
#                 flowerbed[i] = 1
#                 if availablePlots >= n:
#                     return True
#     return availablePlots >= n
