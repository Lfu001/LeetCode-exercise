#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

import bisect
import math
from collections import deque
from typing import List


# @lc code=start
# Solution 4 (Single scan: collections.deque and bisect.insort)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 38.45 % of python3 submissions
# Your memory usage beats 22.92 % of python3 submissions (15.2 MB)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        threeLargest = deque([float("-inf")] * 3)
        twoSmallest = deque([float("inf")] * 2)

        for n in nums:
            bisect.insort(threeLargest, n)
            threeLargest.popleft()
            bisect.insort(twoSmallest, n)
            twoSmallest.pop()

        return max(math.prod(threeLargest), (math.prod(twoSmallest) * threeLargest[-1]))

# @lc code=end

# Solution 1 (Brute force) Time Limit Exceeded
# Time complexity: O(n^3), Space complexity: O(1)

# def maximumProduct(self, nums: List[int]) -> int:
#     return max(map(math.prod, itertools.combinations(nums, 3)))


# Solution 2 (Sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 82.05 % of python3 submissions
# Your memory usage beats 97.79 % of python3 submissions (15.1 MB)

# def maximumProduct(self, nums: List[int]) -> int:
#     nums = sorted(nums)
#     return max(math.prod(nums[-3:]), (nums[0] * nums[1] * nums[-1]))


# Solution 3 (Single scan: find 3 largest and 2 smallest)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 83.87 % of python3 submissions
# Your memory usage beats 72.1 % of python3 submissions (15.1 MB)

# def maximumProduct(self, nums: List[int]) -> int:
#     min1 = min2 = float("inf")
#     max1 = max2 = max3 = float("-inf")
#
#     for n in nums:
#         if n > max3:
#             if n >= max2:
#                 max3 = max2
#                 if n >= max1:
#                     max2 = max1
#                     max1 = n
#                 else:
#                     max2 = n
#             else:
#                 max3 = n
#         if n < min2:
#             if n <= min1:
#                 min2 = min1
#                 min1 = n
#             else:
#                 min2 = n
#
#     return max((max1 * max2 * max3), (max1 * min1 * min2))
