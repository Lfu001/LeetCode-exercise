#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

from typing import List


# @lc code=start
# Solution 4 (Binary search: iterative)
# Time complexity: O(logn), Space complexity: O(1)
# Your runtime beats 22.66 % of python3 submissions
# Your memory usage beats 59.76 % of python3 submissions (15.2 MB)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


# @lc code=end

# Solution 1 (Max)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 25.78 % of python3 submissions
# Your memory usage beats 39.63 % of python3 submissions (15.3 MB)

# def peakIndexInMountainArray(self, arr: List[int]) -> int:
#     return max(range(len(arr)), key=arr.__getitem__)


# Solution 2 (Linear search)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 68.56 % of python3 submissions
# Your memory usage beats 19.75 % of python3 submissions (15.6 MB)

# def peakIndexInMountainArray(self, arr: List[int]) -> int:
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return i


# Solution 3 (Binary search: recursive)
# Time complexity: O(logn), Space complexity: O(logn)
# Your runtime beats 8.48 % of python3 submissions
# Your memory usage beats 19.75 % of python3 submissions (16.2 MB)

# def peakIndexInMountainArray(self, arr: List[int]) -> int:
#     def binarySearch(left, right):
#         mid = left + (right - left) // 2
#         if arr[mid] < arr[mid + 1]:
#             return binarySearch((mid + 1), right)
#         elif arr[mid - 1] > arr[mid]:
#             return binarySearch(left, (mid - 1))
#         else:
#             return mid
#
#     return binarySearch(0, len(arr))
