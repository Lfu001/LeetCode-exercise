#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
# Solution 2 (Marking index)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 68.38 % of python3 submissions
# Your memory usage beats 88.61 % of python3 submissions (21.9 MB)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            index = int(n) - 1
            nums[index] = float(nums[index])

        ans = []

        for i, n in enumerate(nums):
            if isinstance(n, int):
                ans.append(i + 1)
            else:
                nums[i] = int(nums[i])

        return ans

# @lc code=end

# Solution 1 (Set sub)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 30.35 % of python3 submissions
# Your memory usage beats 16.97 % of python3 submissions (26.1 MB)

# def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#     return list(set(range(1, (len(nums) + 1))) - set(nums))
