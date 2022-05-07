#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

import itertools


# @lc code=start
# Solution 2 (Reversed generator)
# Time complexity: O(m+n), Space complexity: O(1)
# Your runtime beats 86.19 % of python3 submissions
# Your memory usage beats 74.9 % of python3 submissions (13.8 MB)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reversedTextGenerator(typed):
            backspaceCounter = 0
            for c in reversed(typed):
                if c == "#":
                    backspaceCounter += 1
                elif backspaceCounter:
                    backspaceCounter -= 1
                else:
                    yield c

        return all(
            a == b
            for a, b in itertools.zip_longest(
                reversedTextGenerator(s), reversedTextGenerator(t)
            )
        )


# @lc code=end

# Solution 1 (Simulation)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 67.16 % of python3 submissions
# Your memory usage beats 74.91 % of python3 submissions (13.8 MB)

# def backspaceCompare(self, s: str, t: str) -> bool:
#     typed = {"s": [], "t": []}
#     for seq, stack in zip((s, t), typed.values()):
#         for c in seq:
#             if c != "#":
#                 stack.append(c)
#             elif stack:
#                 stack.pop()
#     return typed["s"] == typed["t"]
