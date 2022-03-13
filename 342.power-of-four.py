#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# Solution 4 (Bit manipulation)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 29.21 % of python3 submissions
# Your memory usage beats 34.39 % of python3 submissions (13.9 MB)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1) == 0) and (0x55555555 & n == n)

# @lc code=end

# Solution 1 (Loop)
# Time complexity: O(log4(n)), Space complexity: O(1)
# Your runtime beats 11.54 % of python3 submissions
# Your memory usage beats 68.92 % of python3 submissions (13.9 MB)

# def isPowerOfFour(self, n: int) -> bool:
#     while n > 1:
#         n /= 4
#     return n == 1


# Solution 2 (Recursion)
# Time complexity: O(log4(n)), Space complexity: O(1)
# Your runtime beats 39.31 % of python3 submissions
# Your memory usage beats 68.92 % of python3 submissions (13.8 MB)

# def isPowerOfFour(self, n: int) -> bool:
#     if n <= 1:
#         return n == 1
#     else:
#         return self.isPowerOfFour(n / 4)


# Solution 3 (Convert to quaternary)
# Time complexity: O(log4(n)), Space complexity:O(1)
# Your runtime beats 21.34 % of python3 submissions
# Your memory usage beats 25.13 % of python3 submissions (14 MB)

# def isPowerOfFour(self, n: int) -> bool:
#     if n >= 1:
#         n_base4 = self.encode(n, 4)
#         return int(n_base4[0]) == 1 and n_base4.count("0") == (len(n_base4) - 1)
#     else:
#         return False
#
# def encode(self, value: int, base: int):
#     if value >= base:
#         return self.encode((value // base), base) + str(value % base)
#     return str(value % base)
