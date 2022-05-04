#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

from typing import List


# @lc code=start
# Solution 2 (Without built-in function)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 30.3 % of python3 submissions
# Your memory usage beats 28.89 % of python3 submissions (14 MB)
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        s += "."
        groupLength = 1
        head = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if groupLength >= 3:
                    ans.append([head, (head + groupLength - 1)])
                groupLength = 0
                head = i
            groupLength += 1
        return ans


# @lc code=end

# Solution 1 (Built-in: itertools.groupby)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 28.73 % of python3 submissions
# Your memory usage beats 76.45 % of python3 submissions (13.8 MB)

# def largeGroupPositions(self, s: str) -> List[List[int]]:
#     ans = []
#     index = 0
#     for _, group in groupby(s):
#         groupLength = len(list(group))
#         if groupLength >= 3:
#             ans.append([index, (index + groupLength - 1)])
#         index += groupLength
#     return ans
