#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
# Solution 4 (Binary search)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 48.64 % of python3 submissions
# Your memory usage beats 64.86 % of python3 submissions (13.8 MB)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            k = left + (right - left) // 2
            numOfCoinsToBuildKSteps = int(0.5 * k * (k + 1))
            if numOfCoinsToBuildKSteps == n:
                return k
            elif numOfCoinsToBuildKSteps < n:
                left = k + 1
            else:
                right = k - 1

        return right

# @lc code=end

# Solution 1 (Greedy)
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 28.78 % of python3 submissions
# Your memory usage beats 64.86 % of python3 submissions (13.8 MB)

# def arrangeCoins(self, n: int) -> int:
#     numOfCompleteRows = 0
#     numOfCoinsToBuildRowK = 0
#     while True:
#         numOfCoinsToBuildRowK += 1
#         n -= numOfCoinsToBuildRowK
#         if n >= 0:
#             numOfCompleteRows += 1
#         else:
#             break
#     return numOfCompleteRows


# Solution 2 (Math 1)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 95.05 % of python3 submissions
# Your memory usage beats 64.86 % of python3 submissions (13.8 MB)

# def arrangeCoins(self, n: int) -> int:
#     numOfCompleteRows = int((2 * n) ** 0.5)
#     if n < 0.5 * numOfCompleteRows * (numOfCompleteRows + 1):
#         numOfCompleteRows -= 1
#     return numOfCompleteRows


# Solution 3 (Math 2)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 70.37 % of python3 submissions
# Your memory usage beats 97.41 % of python3 submissions (13.8 MB)

# def arrangeCoins(self, n: int) -> int:
#     return int((2 * n + 0.25) ** 0.5 - 0.5)
