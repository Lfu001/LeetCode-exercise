#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
# Solution 3
# Your runtime beats 19.48 % of python3 submissions
# Your memory usage beats 73.95 % of python3 submissions (13.8 MB)
class Solution:
    def isUgly(self, n: int) -> bool:
        return n > 0 == 30 ** 31 % n

# @lc code=end

# Solution 1
# Your runtime beats 90.53 % of python3 submissions
# Your memory usage beats 41.03 % of python3 submissions (14 MB)

# def isUgly(self, n: int) -> bool:
#     while n >= 1:
#         if n % 2 == 0:
#             n /= 2
#             continue
#         if n % 3 == 0:
#             n /= 3
#             continue
#         if n % 5 == 0:
#             n /= 5
#             continue
#         if n == 1:
#             return True
#         else:
#             break
#     return False


# Solution 2
# Your runtime beats 44.98 % of python3 submissions
# Your memory usage beats 73.95 % of python3 submissions (13.8 MB)

# def isUgly(self, n: int) -> bool:
#     if n > 1:
#         for p in [2, 3, 5]:
#             while n % p == 0:
#                 n /= p
#     return n == 1
