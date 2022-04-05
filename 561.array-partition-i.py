#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#

from typing import List


# @lc code=start
# Solution 4 (Sort: bucket sort)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 48.61 % of python3 submissions
# Your memory usage beats 81.2 % of python3 submissions (16.7 MB)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        bucket = [0] * 20001

        for n in nums:
            bucket[n + 10000] += 1

        sum_ = 0
        pickNext = True

        for i in range(20001):
            while bucket[i] > 0:
                if pickNext:
                    sum_ += i - 10000
                pickNext = not pickNext
                bucket[i] -= 1

        return sum_

# @lc code=end

# Solution 1 (Sort: safe)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 54.68 % of python3 submissions
# Your memory usage beats 54.44 % of python3 submissions (16.8 MB)

# def arrayPairSum(self, nums: List[int]) -> int:
#     nums = sorted(nums)
#     return sum(nums[i] for i in range(0, len(nums), 2))


# Solution 2 (Sort: destroy array)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 7.51 % of python3 submissions
# Your memory usage beats 19.67 % of python3 submissions (16.9 MB)

# def arrayPairSum(self, nums: List[int]) -> int:
#     nums.sort()
#     return sum(nums[i] for i in range(0, len(nums), 2))


# Solution 3 (Sort: one-liner)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 56.49 % of python3 submissions
# Your memory usage beats 81.2 % of python3 submissions (16.7 MB)

# def arrayPairSum(self, nums: List[int]) -> int:
#     return sum(sorted(nums)[::2])
