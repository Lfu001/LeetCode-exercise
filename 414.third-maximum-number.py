#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
# Solution 3 (Compare and swap: eliminate duplicates first)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 69.45 % of python3 submissions
# Your memory usage beats 45.95 % of python3 submissions (15.4 MB)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = secondMax = thirdMax = float("-inf")
        nums = list(set(nums))

        for n in nums:
            if n > firstMax:
                firstMax, n = n, firstMax
            if n > secondMax:
                secondMax, n = n, secondMax
            if n > thirdMax:
                thirdMax, n = n, thirdMax

        return thirdMax if thirdMax != float("-inf") else firstMax

# @lc code=end

# Solution 1 (Set and sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 6.88 % of python3 submissions
# Your memory usage beats 45.95 % of python3 submissions (15.4 MB)

# def thirdMax(self, nums: List[int]) -> int:
#     nums = sorted(list(set(nums)))
#     return nums[-3] if len(nums) >= 3 else nums[-1]


# Solution 2 (Iterate set)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 31.6 % of python3 submissions
# Your memory usage beats 45.95 % of python3 submissions (15.4 MB)

# def thirdMax(self, nums: List[int]) -> int:
#     nums = set(nums)
#
#     if len(nums) < 3:
#         return max(nums)
#
#     firstMax = secondMax = thirdMax = -0xffffffff
#
#     while nums:
#         n = nums.pop()
#         if n > firstMax:
#             thirdMax = secondMax
#             secondMax = firstMax
#             firstMax = n
#         elif n > secondMax:
#             thirdMax = secondMax
#             secondMax = n
#         elif n > thirdMax:
#             thirdMax = n
#
#     return thirdMax


# Solution 3 (Compare and swap)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 8.54 % of python3 submissions
# Your memory usage beats 88.08 % of python3 submissions (14.7 MB)

# def thirdMax(self, nums: List[int]) -> int:
#     firstMax = secondMax = thirdMax = float("-inf")
#
#     for n in nums:
#         if n in (firstMax, secondMax, thirdMax):
#             continue
#         if n > firstMax:
#             firstMax, n = n, firstMax
#         if n > secondMax:
#             secondMax, n = n, secondMax
#         if n > thirdMax:
#             thirdMax, n = n, thirdMax
#
#     return thirdMax if thirdMax != float("-inf") else firstMax
