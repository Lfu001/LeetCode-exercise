#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

from typing import List


# @lc code=start
# Solution 3 (dict)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 48.51 % of python3 submissions
# Your memory usage beats 84.51 % of python3 submissions (16.1 MB)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        uniqueCandyTypes = dict()
        for candy in candyType:
            if candy not in uniqueCandyTypes:
                uniqueCandyTypes[candy] = 1
        numOfCandyTypes = len(uniqueCandyTypes)
        numOfCandyAliceCanEat = len(candyType) // 2
        return min(numOfCandyTypes, numOfCandyAliceCanEat)

# @lc code=end

# Solution 1 (set)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 5.06 % of python3 submissions
# Your memory usage beats 71.75 % of python3 submissions (16.1 MB)

# def distributeCandies(self, candyType: List[int]) -> int:
#     numOfCandyTypes = len(set(candyType))
#     numOfCandyAliceCanEat = len(candyType) // 2
#     return min(numOfCandyTypes, numOfCandyAliceCanEat)


# Solution 2 (collections.Counter)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 84.09 % of python3 submissions
# Your memory usage beats 84.51 % of python3 submissions (16 MB)

# def distributeCandies(self, candyType: List[int]) -> int:
#     numOfCandyTypes = len(Counter(candyType))
#     numOfCandyAliceCanEat = len(candyType) // 2
#     return min(numOfCandyTypes, numOfCandyAliceCanEat)
