#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

from typing import List


# @lc code=start
# Solution 2 (Hash map)
# Time complexity: O(n+m), Space complexity: O(n+m)
# Your runtime beats 66.06 % of python3 submissions
# Your memory usage beats 10.72 % of python3 submissions (14.6 MB)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commonInterest = set(list1) & set(list2)
        restaurantToIndex1 = {val: idx for idx, val in enumerate(list1)}
        restaurantToIndex2 = {val: idx for idx, val in enumerate(list2)}
        leastListIndexSum = float("inf")
        for restaurant in commonInterest:
            indexSum = restaurantToIndex1[restaurant] + restaurantToIndex2[restaurant]
            if indexSum < leastListIndexSum:
                leastListIndexSum = indexSum
                ans = [restaurant]
            elif indexSum == leastListIndexSum:
                ans.append(restaurant)
        return ans

# @lc code=end

# Solution 1 (Built-in: set and list.index)
# Time complexity: O(min(n,m)*(n+m)), Space complexity: O(n+m)
# Your runtime beats 19.9 % of python3 submissions
# Your memory usage beats 45.38 % of python3 submissions (14.5 MB)

# def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#     commonInterest = set(list1) & set(list2)
#     leastListIndexSum = float("inf")
#     for restaurant in commonInterest:
#         indexSum = list1.index(restaurant) + list2.index(restaurant)
#         if indexSum < leastListIndexSum:
#             leastListIndexSum = indexSum
#             ans = [restaurant]
#         elif indexSum == leastListIndexSum:
#             ans.append(restaurant)
#     return ans
