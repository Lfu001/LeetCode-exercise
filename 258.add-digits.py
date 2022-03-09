#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
# Solution 3 (Mathematical: Digital Root)
# Reference: https://en.wikipedia.org/wiki/Digital_root
# Your runtime beats 11.28 % of python3 submissions
# Your memory usage beats 17.26 % of python3 submissions (13.9 MB)
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num != 0 else 0

# @lc code=end

# Solution 1 (Loop)
# Your runtime beats 71.6 % of python3 submissions
# Your memory usage beats 61.21 % of python3 submissions (13.8 MB)

# def addDigits(self, num: int) -> int:
#     while num > 9:
#         num = sum(int(i) for i in str(num))
#     return num


# Solution 2 (Recursive)
# Your runtime beats 62.94 % of python3 submissions
# Your memory usage beats 61.21 % of python3 submissions (13.8 MB)

# def addDigits(self, num: int) -> int:
#     if num <= 9:
#         return num
#     else:
#         return self.addDigits(sum(int(i) for i in str(num)))
