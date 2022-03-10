#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Solution 2 (Binary search: Recursive)
# Your runtime beats 94.82 % of python3 submissions
# Your memory usage beats 43.58 % of python3 submissions (13.9 MB)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, left: int, right: int) -> int:
        if left >= right:
            return right

        mid = left + (right - left) // 2

        if isBadVersion(mid):
            return self.binarySearch(left, mid)
        else:
            return self.binarySearch((mid + 1), right)

# @lc code=end

# This can cause OVERFLOW.
# mid = (left + right) // 2

# To avoid overflow, we should get `mid` like this.
# mid = left + (right - left) // 2


# Solution 1 (Binary search: Iterative)
# Your runtime beats 65.6 % of python3 submissions
# Your memory usage beats 77.67 % of python3 submissions (13.8 MB)

# def firstBadVersion(self, n: int) -> int:
#     left = 1
#     right = n
#     while left < right:
#         mid = left + (right - left) // 2
#         if isBadVersion(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return right
