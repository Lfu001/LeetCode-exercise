#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        if p1 > p2:
            return 0

        while p1 < p2:
            if nums[p1] != val:
                p1 += 1
            if nums[p2] == val:
                nums[p2] = None
                p2 -= 1
            if nums[p1] == val and nums[p2] != val:
                nums[p1] = nums[p2]
                nums[p2] = None
                p1 += 1
                p2 -= 1

        if p1 == p2:
            return p1 if nums[p1] == val else p1 + 1
        else:
            return p2 if nums[p2] == val else p2 + 1

# @lc code=end
