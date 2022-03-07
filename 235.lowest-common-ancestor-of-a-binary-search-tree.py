#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 2 (Iterative)
# Your runtime beats 68.14 % of python3 submissions
# Your memory usage beats 15.71 % of python3 submissions (18.8 MB)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

# @lc code=end

# Solution 1 (Recursive)
# Your runtime beats 38.14 % of python3 submissions
# Your memory usage beats 45.34 % of python3 submissions (18.7 MB)

# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#     if p.val < root.val > q.val:
#         return self.lowestCommonAncestor(root.left, p, q)
#     if p.val > root.val < q.val:
#         return self.lowestCommonAncestor(root.right, p, q)
#     return root
