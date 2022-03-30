#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
# Reference: https://cp-algorithms.com/algebra/divisors.html#toc-tgt-1
# Solution 3 (Sum up divisors using formula))
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 20.63 % of python3 submissions
# Your memory usage beats 61.31 % of python3 submissions (13.9 MB)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return self.divisorFunc(num) == 2 * num

    def divisorFunc(self, num: int) -> int:
        sum = 1
        for i in range(2, (int(num ** 0.5) + 1)):
            c = 1
            while num % i == 0:
                c += 1
                num //= i
            sum *= (i ** c - 1) // (i - 1)
        if num != 1:
            sum *= 1 + num
        return sum

# @lc code=end

# Solution 1 (Search from known perfect numbers)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 78.9 % of python3 submissions
# Your memory usage beats 61.31 % of python3 submissions (13.9 MB)

# def checkPerfectNumber(self, num: int) -> bool:
#     return num in {6, 28, 496, 8128, 33550336}


# Solution 2 (Sum up divisors one by one))
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 86.64 % of python3 submissions
# Your memory usage beats 15.12 % of python3 submissions (13.9 MB)

# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         return self.divisorFunc(num) == 2 * num
#
#     def divisorFunc(self, num: int) -> int:
#         if num == 1:
#             return 1
#         sum = 0
#         for i in range(1, (int(sqrt(num)) + 1)):
#             if num % i == 0:
#                 sum += i + (num // i)
#         return sum
