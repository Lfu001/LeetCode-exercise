#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
# Solution 4 (Covert to ternary)
# Your runtime beats 24.59 % of python3 submissions
# Your memory usage beats 42.66 % of python3 submissions (13.9 MB)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        n_base3 = self.encode(n, 3)
        return n >= 1 == int(n_base3[0]) and n_base3.count("0") == (len(n_base3) - 1)

    def encode(self, value: int, base: int):
        if value >= base:
            return self.encode((value // base), base) + str(value % base)
        return str(value % base)

# @lc code=end

# Solution 1 (Loop)
# Your runtime beats 83.93 % of python3 submissions
# Your memory usage beats 42.66 % of python3 submissions (14 MB)

# def isPowerOfThree(self, n: int) -> bool:
#     while n > 1:
#         n /= 3
#     return n == 1


# Solution 2 (Recursion)
# Your runtime beats 55.03 % of python3 submissions
# Your memory usage beats 73.1 % of python3 submissions (13.9 MB)

# def isPowerOfThree(self, n: int) -> bool:
#     if n <= 1:
#         return n == 1
#     else:
#         return self.isPowerOfThree(n / 3)


# Solution 3 (Division)
# Your runtime beats 26.96 % of python3 submissions
# Your memory usage beats 73.1 % of python3 submissions (13.9 MB)

# def isPowerOfThree(self, n: int) -> bool:
#     # 3486784401 == 3 ** 20
#     return n >= 1 and 3486784401 % n == 0
