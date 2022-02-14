#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]

# @lc code=end

# Solution 1
# num = 0
# for i in digits:
#     num *= 10
#     num += i
# num += 1
# return [int(i) for i in str(num)]
