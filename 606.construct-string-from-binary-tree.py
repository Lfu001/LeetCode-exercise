#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 27.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.1 MB)
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node in {"(", ")"}:
                    ans += node
                    continue
                ans += str(node.val)
                if node.left or node.right:
                    if node.right:
                        stack.append(")")
                        stack.append(node.right)
                        stack.append("(")
                    stack.append(")")
                    stack.append(node.left)
                    stack.append("(")
        return ans

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 48.92 % of python3 submissions
# Your memory usage beats 71.41 % of python3 submissions (16.3 MB)

# def tree2str(self, root: Optional[TreeNode]) -> str:
#     if not root:
#         return ""
#     else:
#         left = self.tree2str(root.left)
#         right = self.tree2str(root.right)
#         res = str(root.val)
#         if left or right:
#             res += "(" + left + ")"
#             if right:
#                 res += "(" + right + ")"
#         return res
