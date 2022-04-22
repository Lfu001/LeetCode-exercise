#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

from re import match


# @lc code=start
# Solution 4 (Regex)
# Time complexity: O(1), Space complexity: (1)
# Your runtime beats 84.16 % of python3 submissions
# Your memory usage beats 57.85 % of python3 submissions (13.9 MB)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return match("^(10)*1?$", format(n, "b"))

# @lc code=end

# Solution 1 (Xor)
# Time complexity: O(1), Space complexity: (1)
# Your runtime beats 85.29 % of python3 submissions
# Your memory usage beats 10.18 % of python3 submissions (13.9 MB)

# def hasAlternatingBits(self, n: int) -> bool:
#     binary = list(map(int, format(n, "b")))
#     return all(binary[i] ^ binary[i + 1] for i in range(len(binary) - 1))


# Solution 2 (String comparison)
# Time complexity: O(1), Space complexity: (1)
# Your runtime beats 30.55 % of python3 submissions
# Your memory usage beats 57.85 % of python3 submissions (13.8 MB)

# def hasAlternatingBits(self, n: int) -> bool:
#     binary = format(n, "b")
#     return all(binary[i] != binary[i + 1] for i in range(len(binary) - 1))


# Solution 3 (Cancel bits)
# Time complexity: O(1), Space complexity: (1)
# Your runtime beats 25.18 % of python3 submissions
# Your memory usage beats 95.9 % of python3 submissions (13.8 MB)

# def hasAlternatingBits(self, n: int) -> bool:
#     n ^= (n >> 2)
#     return not (n & (n - 1))
