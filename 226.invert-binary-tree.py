#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 4 (Recursive)
# Your runtime beats 98.86 % of python3 submissions
# Your memory usage beats 52.78 % of python3 submissions (13.9 MB)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# @lc code=end

# Solution 1 (Recursive)
# Your runtime beats 57.55 % of python3 submissions
# Your memory usage beats 79.27 % of python3 submissions (13.8 MB)

# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#     if root:
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#     return root


# Solution 2 (Recursive)
# Your runtime beats 49.68 % of python3 submissions
# Your memory usage beats 79.27 % of python3 submissions (13.9 MB)

# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#     if root:
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#     return root


# Solution 3 (Iterative)
# Your runtime beats 95.24 % of python3 submissions
# Your memory usage beats 79.27 % of python3 submissions (13.8 MB)

# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node:
#             stack.append(node.left)
#             stack.append(node.right)
#             node.left, node.right = node.right, node.left
#     return root
