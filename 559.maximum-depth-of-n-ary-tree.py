#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 40.81 % of python3 submissions
# Your memory usage beats 6.74 % of python3 submissions (16.2 MB)
class Solution:
    def maxDepth(self, root: Optional["Node"]) -> int:
        maxDepth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if not node:
                return maxDepth
            elif node.children:
                stack += [(child, (depth + 1)) for child in node.children]
            else:
                maxDepth = max(maxDepth, depth)

        return maxDepth

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 87.8 % of python3 submissions
# Your memory usage beats 6.74 % of python3 submissions (16.2 MB)

# def maxDepth(self, root: Optional["Node"]) -> int:
#     if not root:
#         return 0
#     elif not root.children:
#         return 1
#     else:
#         return max(map(self.maxDepth, root.children)) + 1
