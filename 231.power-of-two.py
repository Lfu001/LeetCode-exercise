#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
# Solution 3 (Bit manipulation)
# Your runtime beats 89.6 % of python3 submissions
# Your memory usage beats 50.35 % of python3 submissions (13.9 MB)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and format(n, "b").count("1") == 1

# @lc code=end

# Solution 1 (Recursive)
# Your runtime beats 25.93 % of python3 submissions
# Your memory usage beats 76.24 % of python3 submissions (13.8 MB)

# def isPowerOfTwo(self, n: int) -> bool:
#     if n < 1:
#         return False
#     elif n == 1:
#         return True
#     else:
#         return self.isPowerOfTwo(n / 2)

# Solution 2 (Loop)
# Your runtime beats 6.17 % of python3 submissions
# Your memory usage beats 97.7 % of python3 submissions (13.8 MB)
# def isPowerOfTwo(self, n: int) -> bool:
#     while n >= 1:
#         if n == 1:
#             return True
#         n /= 2
#     return False
