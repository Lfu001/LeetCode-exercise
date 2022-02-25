#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# Your runtime beats 54.44 % of python3 submissions
# Your memory usage beats 57.31 % of python3 submissions (14 MB)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += n & 1
            n >>= 1
        return count

# @lc code=end

# Solution 1
# Your runtime beats 87.53 % of python3 submissions
# Your memory usage beats 57.31 % of python3 submissions (13.9 MB)

# def hammingWeight(self, n: int) -> int:
#     count = 0
#     for n in format(n, "b"):
#         count += int(n)
#     return count
