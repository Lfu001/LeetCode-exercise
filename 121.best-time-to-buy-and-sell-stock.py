#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_ = 0
        for i in range(1, len(prices)):
            min_ = min(min_, prices[i])
            max_ = max(max_, prices[i] - min_)
        return max_

# @lc code=end

# Solution 1 (Time Exceeded)
# profit = 0
# for i in range(1, len(prices)):
#     for j in range(i):
#         diff = prices[i] - prices[j]
#         print("{} - {} = {}".format(prices[j], prices[i], diff))
#         if diff > profit:
#             profit = diff
# return profit


# Solution 2
# profit = 0
# max_ = 0
# for i in range(1, len(prices)):
#     t = prices[i] - prices[i - 1]
#     profit = max(t, (profit + t))
#     max_ = max(max_, profit)
# return max_
