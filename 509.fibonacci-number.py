#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
# Solution 6 (Math: general term (matrix))
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 29.67 % of python3 submissions
# Your memory usage beats 11.39 % of python3 submissions (32 MB)
import numpy as np


class Solution:
    def fib(self, n: int) -> int:
        return np.linalg.matrix_power(np.array([[1, 1], [1, 0]]), n)[0, 1]

# @lc code=end

# Solution 1 (Recursive: greedy)
# Time complexity: O(((1+√(5))/2)^n), Space complexity: O(1)
# Your runtime beats 13.31 % of python3 submissions
# Your memory usage beats 96.25 % of python3 submissions (13.7 MB)

# def fib(self, n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return self.fib(n - 1) + self.fib(n - 2)

# Solution 2 (Recursive: using functools.lru_cache)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 65.68 % of python3 submissions
# Your memory usage beats 58.73 % of python3 submissions (13.9 MB)

# @lru_cache
# def fib(self, n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return self.fib(n - 1) + self.fib(n - 2)

# Solution 3 (Iterative)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 51.24 % of python3 submissions
# Your memory usage beats 11.39 % of python3 submissions (13.9 MB)

# def fib(self, n: int) -> int:
#     prev = 0
#     current = 1
#     for _ in range(n - 1):
#         prev, current = current, (current + prev)
#     return n and current


# Solution 4 (Math: general term)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 96.24 % of python3 submissions
# Your memory usage beats 96.25 % of python3 submissions (13.8 MB)

# def fib(self, n: int) -> int:
#     return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5)


# Solution 5 (Math: general term (approximate expression))
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 57.06 % of python3 submissions
# Your memory usage beats 11.39 % of python3 submissions (14 MB)

# def fib(self, n: int) -> int:
#     return int((((1 + 5 ** 0.5) / 2) ** n) / 5 ** 0.5 + 0.5)
