#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
# Solution 2 (Replace Solution 1's prime number set to int value 665772(=0b10100010100010101100))
# Time complexity: O(right - left), Space complexity: O(1)
# Your runtime beats 58.11 % of python3 submissions
# Your memory usage beats 27.27 % of python3 submissions (14 MB)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(
            665772 >> bin(num).count("1") & 1 for num in range(left, (right + 1))
        )


# @lc code=end

# Solution 1 (Built-in: bin and count)
# Time complexity: O(right - left), Space complexity: O(1)
# Your runtime beats 87.52 % of python3 submissions
# Your memory usage beats 78.25 % of python3 submissions (13.8 MB)

# def countPrimeSetBits(self, left: int, right: int) -> int:
#     count = 0
#     for num in range(left, (right + 1)):
#         if bin(num).count("1") in {2, 3, 5, 7, 11, 13, 17, 19}:
#             count += 1
#     return count
