#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
# Solution 4 (Bit manipulation: count manually bitAnd(&) trick)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 9.21 % of python3 submissions
# Your memory usage beats 67.02 % of python3 submissions (13.8 MB)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x_xor_y = x ^ y
        while x_xor_y > 0:
            count += 1
            x_xor_y &= x_xor_y - 1
        return count

# @lc code=end

# Solution 1 (Bit manipulation: bin and str.count)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 5.99 % of python3 submissions
# Your memory usage beats 20.44 % of python3 submissions (13.9 MB)

# def hammingDistance(self, x: int, y: int) -> int:
#     return bin(x ^ y).count("1")


# Solution 2 (Bit manipulation: format and str.count)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 61.55 % of python3 submissions
# Your memory usage beats 67.02 % of python3 submissions (13.8 MB)

# def hammingDistance(self, x: int, y: int) -> int:
#     return format((x ^ y), "b").count("1")


# Solution 3 (Bit manipulation: count manually with bitAnd(&) and bitShift(>>))
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 30.83 % of python3 submissions
# Your memory usage beats 20.44 % of python3 submissions (13.9 MB)

# def hammingDistance(self, x: int, y: int) -> int:
#     count = 0
#     x_xor_y = x ^ y
#     for _ in range(32):
#         count += x_xor_y & 1
#         x_xor_y >>= 1
#     return count
