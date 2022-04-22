#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

from typing import List


# @lc code=start
# Solution 1 (Stack)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 96.95 % of python3 submissions
# Your memory usage beats 5.17 % of python3 submissions (14.2 MB)
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for operation in ops:
            if operation == "+":
                stack.append(stack[-2] + stack[-1])
            elif operation == "D":
                stack.append(2 * stack[-1])
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)

# @lc code=end
