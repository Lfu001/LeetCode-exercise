#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right or (left.val != right.val):
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))

        return True

# @lc code=end

# Solution 1
# def isSymmetricTree(p, q):
#     if p and q:
#         if p.val != q.val:
#             return False
#         else:
#             return isSymmetricTree(p.left, q.right) and isSymmetricTree(p.right, q.left)
#     elif not p and not q:
#         return True
#     else:
#         return False
# return isSymmetricTree(root.left, root.right)
