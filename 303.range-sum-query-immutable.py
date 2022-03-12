#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
# Solution 2 (Dynamic programming: create new array)
# Your runtime beats 82.94 % of python3 submissions
# Your memory usage beats 12.61 % of python3 submissions (17.8 MB)
class NumArray:

    def __init__(self, nums: List[int]):
        self.cumSum = [0]
        for num in nums:
            self.cumSum.append(self.cumSum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumSum[right + 1] - self.cumSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

# Solution 1 (Calculate sum every time `sumRange()` called)
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 97.32 % of python3 submissions (17.4 MB)

# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[i] for i in range(left, (right + 1)))
