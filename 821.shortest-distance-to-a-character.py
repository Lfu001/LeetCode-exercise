#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

from typing import List


# @lc code=start
# Solution 2 (Minimum of left-to-right and right-to-left)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 68.51 % of python3 submissions
# Your memory usage beats 91.94 % of python3 submissions (13.9 MB)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        prev = float("-inf")
        for i, letter in enumerate(s):
            if letter == c:
                prev = i
            ans.append(i - prev)

        prev = float("inf")
        for i in range((len(s) - 1), -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], (prev - i))

        return ans


# @lc code=end

# Solution 1 (Split string)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 90.01 % of python3 submissions
# Your memory usage beats 91.94 % of python3 submissions (13.9 MB)

# def shortestToChar(self, s: str, c: str) -> List[int]:
#     ans = []
#     serialized = s.replace(c, " . ").split()
#     for i, block in enumerate(serialized):
#         if block != ".":
#             halfLength = len(block) // 2
#             oddLength = len(block) & 1
#             if i == 0:
#                 ans += list(range(len(block), 0, -1))
#             elif i == (len(serialized) - 1):
#                 ans += list(range(1, (len(block) + 1)))
#             else:
#                 ans += list(range(1, (halfLength + oddLength + 1)))
#                 ans += list(range(halfLength, 0, -1))
#         else:
#             ans.append(0)
#     return ans
