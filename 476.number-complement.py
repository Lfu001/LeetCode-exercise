#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
# Solution 5 (Bit manipulation: get mask by bit-shift)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 60.64 % of python3 submissions
# Your memory usage beats 15.59 % of python3 submissions (13.9 MB)
class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        for i in [1, 2, 4, 8, 16]:
            mask |= mask >> i
        return num ^ mask

# @lc code=end

# Solution 1 (Bit manipulation: get mask by bit-shift, len and bin)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 28.11 % of python3 submissions
# Your memory usage beats 15.59 % of python3 submissions (13.9 MB)

# def findComplement(self, num: int) -> int:
#     return ((1 << len(bin(num)) - 2) - 1) ^ num


# Solution 2 (Bit manipulation: get mask by str.__mul__, len and bin)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 15.52 % of python3 submissions
# Your memory usage beats 58.1 % of python3 submissions (13.9 MB)

# def findComplement(self, num: int) -> int:
#     return int(("1" * (len(bin(num)) - 2)), 2) ^ num


# Solution 3 (Bit manipulation: get mask by str.__mul__ and int.bit_length)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 77.36 % of python3 submissions
# Your memory usage beats 15.59 % of python3 submissions (13.9 MB)

# def findComplement(self, num: int) -> int:
#     return int(("1" * num.bit_length()), 2) ^ num


# Solution 4 (Bit manipulation: get mask by bit-shift and int.bit_length)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 94.53 % of python3 submissions
# Your memory usage beats 15.59 % of python3 submissions (13.9 MB)

# def findComplement(self, num: int) -> int:
#     return ((1 << num.bit_length()) - 1) ^ num
