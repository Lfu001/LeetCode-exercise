#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from itertools import groupby


# Solution 5 (Using itertools.groupby)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 99.59 % of python3 submissions
# Your memory usage beats 83.84 % of python3 submissions (14.2 MB)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(sum(group) for key, group in groupby(nums))

# @lc code=end

# Solution 1 (Compare sub-array cumulative sums)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 73.72 % of python3 submissions
# Your memory usage beats 83.84 % of python3 submissions (14.2 MB)

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     cumsum = maxNumOfConsecutiveOnes = 0
#     for i in range(len(nums)):
#         cumsum += nums[i]
#         if (i + 1) == len(nums) or nums[i] == 0:
#             if cumsum > maxNumOfConsecutiveOnes:
#                 maxNumOfConsecutiveOnes = cumsum
#             cumsum = 0
#     return maxNumOfConsecutiveOnes


# Solution 2 (Kadane's algorithm)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 8.6 % of python3 submissions
# Your memory usage beats 83.84 % of python3 submissions (14.3 MB)

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     if len(nums) == 1:
#         return nums[0]
#
#     sumOfSubArray = maxNumOfConsecutiveOnes = nums[0]
#
#     for i in range(1, len(nums)):
#         n = nums[i] if nums[i] != 0 else float("-inf")
#         sumOfSubArray = max((sumOfSubArray + n), n)
#         if sumOfSubArray > maxNumOfConsecutiveOnes:
#             maxNumOfConsecutiveOnes = sumOfSubArray
#
#     return maxNumOfConsecutiveOnes


# Solution 3 (Convert to str, split by "0", get maximum number of consecutive 1's)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 48.14 % of python3 submissions
# Your memory usage beats 6.47 % of python3 submissions (15 MB)

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     return max(map(len, "".join(map(str, nums)).split("0")))


# Solution 4 (In-place 1)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 23.65 % of python3 submissions
# Your memory usage beats 6.47 % of python3 submissions (14.6 MB)

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     maxNumOfConsecutiveOnes = nums[0]
#
#     for i in range(1, len(nums)):
#         if nums[i - 1] != 0 == nums[i]:
#             maxNumOfConsecutiveOnes = max(maxNumOfConsecutiveOnes, nums[i - 1], nums[i])
#         else:
#             nums[i] += nums[i - 1]
#             if (i + 1) == len(nums):
#                 maxNumOfConsecutiveOnes = max(maxNumOfConsecutiveOnes, nums[i - 1], nums[i])
#
#     return maxNumOfConsecutiveOnes


# Solution 4 (In-place 2)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 13.23 % of python3 submissions
# Your memory usage beats 10.89 % of python3 submissions (14.4 MB)

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     for i in range(1, len(nums)):
#         if nums[i]:
#             nums[i] += nums[i - 1]
#     return max(nums)
