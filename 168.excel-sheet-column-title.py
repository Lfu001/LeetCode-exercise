#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
# Your runtime beats 26.31 % of python3 submissions
# Your memory usage beats 54.29 % of python3 submissions (13.9 MB)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""

        while columnNumber > 0:
            ans += alphabets[(columnNumber - 1) % 26]
            columnNumber = (columnNumber - 1) // 26

        return ans[::-1]

# @lc code=end

# Solution 1
# Your runtime beats 97.55 % of python3 submissions
# Your memory usage beats 54.29 % of python3 submissions (13.9 MB)

# def convertToTitle(self, columnNumber: int) -> str:
#     n = 0
#     while columnNumber > 26 ** n:
#         n += 1

#     alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     ans = ""

#     for _ in range(n - 1):
#         columnNumber, r = (columnNumber // 26), (columnNumber % 26)
#         if r <= 0:
#             columnNumber -= 1
#             r = 26 - r
#         ans += alphabets[r - 1]

#     if columnNumber != 0:
#         ans += alphabets[columnNumber - 1]

#     return ans[::-1]
