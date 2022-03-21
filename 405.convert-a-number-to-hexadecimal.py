#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
# Solution 1 (Bit manipulation: extend str)
# Time complexity: O(log16(n)), Space complexity: O(1)
# Your runtime beats 73.83 % of python3 submissions
# Your memory usage beats 97.66 % of python3 submissions (13.8 MB)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xffffffff
        ans = ""
        letters = "0123456789abcdef"

        while num:
            ans = letters[num & 0xf] + ans
            num >>= 4

        return ans

# @lc code=end

# Solution 1 (Bit manipulation: Reverse in the end)
# Time complexity: O(log16(n)), Space complexity: O(1)
# Your runtime beats 15.37 % of python3 submissions
# Your memory usage beats 70.94 % of python3 submissions (13.8 MB)

# def toHex(self, num: int) -> str:
#     if num == 0:
#         return "0"
#
#     negativeNum = num < 0
#
#     if negativeNum:
#         num = 0x100000000 + num
#
#     ans = ""
#
#     while num > 0:
#         ans += chr(ord("a") + (t % 10)) if (t := num % 16) > 9 else str(t)
#         num //= 16
#
#     ans = ans[::-1]
#
#     return ans
