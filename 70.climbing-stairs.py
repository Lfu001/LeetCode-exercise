#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 1
        for _ in range(n - 1):
            c = a + b
            a = b
            b = c
        return c

# @lc code=end

# Solution 1
# def factorial(self, n: int, d: int = 0) -> int:
#     """
#     Return
#     ---
#     n! / d!
#     """
#     x = 1
#     for i in (i for i in range(d + 1, n + 1)):
#         x *= i
#     return x

# def climbStairs(self, n: int) -> int:
#     count = 0
#     maxnumOfTimesToClimbTwoSteps = n // 2
#     numOfTimesToClimbTwoSteps = 0
#     while numOfTimesToClimbTwoSteps <= maxnumOfTimesToClimbTwoSteps:
#         k = n - numOfTimesToClimbTwoSteps
#         small, large = sorted([numOfTimesToClimbTwoSteps, k - numOfTimesToClimbTwoSteps])
#         count += self.factorial(k, large) / self.factorial(small)
#         numOfTimesToClimbTwoSteps += 1
#     return int(count)

# Solution 2
# fibonacchi = [1, 1]
# if n == 1:
#     return 1
# for i in range(n - 1):
#     fibonacchi.append(fibonacchi[i] + fibonacchi[i + 1])
# return fibonacchi.pop()
