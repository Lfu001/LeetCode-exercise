#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Solution 1 (Binary search: Recursive)
# Time complexity: O(logn), Space complexity: O(logn)
# Your runtime beats 85.28 % of python3 submissions
# Your memory usage beats 20.48 % of python3 submissions (14 MB)
class Solution:
    def guessNumber(self, n: int) -> int:
        def helper(left, right):
            mid = left + (right - left) // 2
            guessResult = guess(mid)
            if guessResult == -1:
                return helper(left, (mid - 1))
            elif guessResult == 1:
                return helper((mid + 1), right)
            else:
                return mid

        return helper(1, n)

# @lc code=end

# Solution 1 (Binary search: Iterative)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 93.61 % of python3 submissions
# Your memory usage beats 76.9 % of python3 submissions (13.8 MB)

# def guessNumber(self, n: int) -> int:
#     left = 1
#     right = n
#     while True:
#         mid = left + (right - left) // 2
#         guessResult = guess(mid)
#         if guessResult == -1:
#             right = mid - 1
#         elif guessResult == 1:
#             left = mid + 1
#         else:
#             return mid
