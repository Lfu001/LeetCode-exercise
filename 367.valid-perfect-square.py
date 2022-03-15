#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
# Solution 5 (Newton's method)
# Time complexity: ???, Space complexity: O(1)
# Your runtime beats 95.17 % of python3 submissions
# Your memory usage beats 67.66 % of python3 submissions (13.8 MB)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + (num // x)) // 2
        return x * x == num

# @lc code=end

# Solution 1 (Linear search)
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 5.39 % of python3 submissions
# Your memory usage beats 67.66 % of python3 submissions (13.8 MB)

# def isPerfectSquare(self, num: int) -> bool:
#     n = 1
#     square_n = 1
#
#     while square_n <= num:
#         if square_n == num:
#             return True
#         n += 1
#         square_n = n ** 2
#
#     return False


# Solution 2 (Binary search)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 42.89 % of python3 submissions
# Your memory usage beats 67.66 % of python3 submissions (13.8 MB)

# def isPerfectSquare(self, num: int) -> bool:
#     left = 1
#     right = num
#
#     while (left + 1) != right:
#         mid = left + (right - left) // 2
#         mid_squared = mid ** 2
#         if num > mid_squared:
#             left = mid
#         elif num < mid_squared:
#             right = mid
#         else:
#             return True
#
#     return False


# Solution 3 (Bit manipulation)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 78.14 % of python3 submissions
# Your memory usage beats 29.76 % of python3 submissions (13.9 MB)

# def isPerfectSquare(self, num: int) -> bool:
#     root = 0
#     bit = 1 << 15
#     while bit > 0:
#         root |= bit
#         if root > num // root:
#             root ^= bit
#         bit >>= 1
#     return root == num / root


# Solution 4 (Math)
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 5.61 % of python3 submissions
# Your memory usage beats 29.76 % of python3 submissions (13.9 MB)

# def isPerfectSquare(self, num: int) -> bool:
#     k = 1
#     while num > 0:
#         num -= k
#         k += 2
#     return num == 0
