#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

from typing import List


# @lc code=start
# Solution 1 (Two pointers)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 78.54 % of python3 submissions
# Your memory usage beats 71.4 % of python3 submissions (16.3 MB)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        p_even = 0
        p_odd = 1
        while max(p_even, p_odd) < len(nums):
            while p_even < len(nums) and not (nums[p_even] & 1):
                p_even += 2
            while p_odd < len(nums) and (nums[p_odd] & 1):
                p_odd += 2
            if max(p_even, p_odd) < len(nums):
                nums[p_even], nums[p_odd] = nums[p_odd], nums[p_even]
        return nums


# @lc code=end
