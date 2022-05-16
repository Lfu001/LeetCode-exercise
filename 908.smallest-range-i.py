#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

from typing import List


# @lc code=start
# Solution 2 (One pass)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 54.82 % of python3 submissions
# Your memory usage beats 63.81 % of python3 submissions (15.3 MB)
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_nums = float("-inf")
        min_nums = float("inf")
        for n in nums:
            if n > max_nums:
                max_nums = n
            if n < min_nums:
                min_nums = n
        return max(0, (max_nums - min_nums - k * 2))


# @lc code=end

# Solution 1 (Get max and min by built-in functions)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 15.2 % of python3 submissions
# Your memory usage beats 63.81 % of python3 submissions (15.3 MB)

# def smallestRangeI(self, nums: List[int], k: int) -> int:
#     return max(0, (max(nums) - min(nums) - k * 2))
