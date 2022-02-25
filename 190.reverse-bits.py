#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
# Your runtime beats 33.69 % of python3 submissions
# Your memory usage beats 98.07 % of python3 submissions (13.8 MB)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 59.21 % of python3 submissions
# Your memory usage beats 79.11 % of python3 submissions (13.8 MB)

# def reverseBits(self, n: int) -> int:
#     reversed = format(n, "b")[::-1]
#     reversed += "0" * (32 - len(reversed))
#     return int(reversed, 2)
