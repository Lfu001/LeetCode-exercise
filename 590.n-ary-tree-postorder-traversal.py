#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 99 % of python3 submissions
# Your memory usage beats 83.78 % of python3 submissions (16.1 MB)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            stack += node.children
        return ans[::-1]

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 46.29 % of python3 submissions
# Your memory usage beats 20.32 % of python3 submissions (16.5 MB)

# def postorder(self, root: "Node") -> List[int]:
#     if not root:
#         return []
#     else:
#         return sum((self.postorder(child) for child in root.children), start=[]) + [root.val]
