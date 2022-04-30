#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

from typing import List


# @lc code=start
# Solution 2 (Hash map: sliding window)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 42.24 % of python3 submissions
# Your memory usage beats 98.05 % of python3 submissions (13.9 MB)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[:2]
        for i in range(2, len(cost)):
            current = cost[i] + min(prev2, prev1)
            prev2, prev1 = prev1, current
        return min(prev1, prev2)


# @lc code=end

# Solution 1 (Hash map: functools.lru_cache)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 68.26 % of python3 submissions
# Your memory usage beats 15.82 % of python3 submissions (15.9 MB)

# def minCostClimbingStairs(self, cost: List[int]) -> int:
#     @lru_cache
#     def dp(i: int) -> int:
#         if i < 0:
#             return 0
#         elif i <= 1:
#             return cost[i]
#         else:
#             return cost[i] + min(dp(i - 1), dp(i - 2))
#
#     n = len(cost)
#     return min(dp(n - 1), dp(n - 2))
