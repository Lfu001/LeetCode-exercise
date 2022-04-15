#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

from typing import List


# @lc code=start
# Solution 6 (Sum)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 97.4 % of python3 submissions
# Your memory usage beats 36 % of python3 submissions (15.9 MB)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        expectedSum = len(nums) * (len(nums) + 1) // 2
        setSum = sum(set(nums))
        errorSum = sum(nums)
        return [(errorSum - setSum), (expectedSum - setSum)]

# @lc code=end

# Solution 1 (Sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 90.38 % of python3 submissions
# Your memory usage beats 90.99 % of python3 submissions (15.3 MB)

# def findErrorNums(self, nums: List[int]) -> List[int]:
#     nums = sorted(nums)
#     missing = 1
#     for i in range(1, len(nums)):
#         if nums[i] != (nums[i - 1] + 1):
#             if nums[i] == nums[i - 1]:
#                 duplicated = nums[i]
#             elif nums[i] > (nums[i - 1] + 1):
#                 missing = (nums[i - 1] + 1)
#     if nums[-1] != len(nums):
#         missing = len(nums)
#     return [duplicated, missing]


# Solution 2 (Hash map: collections.Counter)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 85.42 % of python3 submissions
# Your memory usage beats 55.23 % of python3 submissions (15.7 MB)

# def findErrorNums(self, nums: List[int]) -> List[int]:
#     counter = Counter(range(1, (len(nums) + 1)))
#     for n in nums:
#         counter[n] -= 1
#     for k, v in counter.items():
#         if v == -1:
#             duplicated = k
#         elif v == 1:
#             missing = k
#     return [duplicated, missing]


# Solution 3 (Hash map: list)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 96.55 % of python3 submissions
# Your memory usage beats 68.42 % of python3 submissions (15.5 MB)

# def findErrorNums(self, nums: List[int]) -> List[int]:
#     counter = [1] * len(nums)
#     for n in nums:
#         counter[n - 1] -= 1
#     for i, v in enumerate(counter):
#         if v == -1:
#             duplicated = i + 1
#         elif v == 1:
#             missing = i + 1
#     return [duplicated, missing]


# Solution 4 (Flag: invert sign)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 72.59 % of python3 submissions
# Your memory usage beats 79.37 % of python3 submissions (15.4 MB)

# def findErrorNums(self, nums: List[int]) -> List[int]:
#     for n in nums:
#         if nums[abs(n) - 1] < 0:
#             duplicated = abs(n)
#         else:
#             nums[abs(n) - 1] *= -1
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             missing = i + 1
#         else:
#             nums[i] *= -1
#     return [duplicated, missing]


# Solution 5 (Bit manipulation)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 66.24 % of python3 submissions
# Your memory usage beats 90.99 % of python3 submissions (15.3 MB)

# def findErrorNums(self, nums: List[int]) -> List[int]:
#     xorOfDupAndMissing = 0
#     for i, n in enumerate(nums):
#         xorOfDupAndMissing ^= (i + 1) ^ n
#
#     rightMostBit = xorOfDupAndMissing & (-xorOfDupAndMissing)
#
#     dupOrMissing = [0, 0]
#     for i, n in enumerate(nums):
#         if (n & rightMostBit) == 0:
#             dupOrMissing[0] ^= n
#         else:
#             dupOrMissing[1] ^= n
#         if ((i + 1) & rightMostBit) == 0:
#             dupOrMissing[0] ^= i + 1
#         else:
#             dupOrMissing[1] ^= i + 1
#
#     if dupOrMissing[0] in nums:
#         return dupOrMissing
#     else:
#         return dupOrMissing[::-1]
