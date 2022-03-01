#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# Your runtime beats 43.69 % of python3 submissions
# Your memory usage beats 5.86 % of python3 submissions (26.1 MB)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

# @lc code=end

# Solution 1
# Your runtime beats 8.34 % of python3 submissions
# Your memory usage beats 31.25 % of python3 submissions (26 MB)

# def containsDuplicate(self, nums: List[int]) -> bool:
#     return len(nums) != len(set(nums))
