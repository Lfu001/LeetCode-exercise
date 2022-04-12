#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
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
# Time complexity: O(N) (N is the number of overlapped nodes), Space complexity: O(min(n,m))
# Your runtime beats 69.67 % of python3 submissions
# Your memory usage beats 47.6 % of python3 submissions (15.6 MB)
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2):
            return root1 or root2

        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val

            if node1.right and node2.right:
                stack.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right

            if node1.left and node2.left:
                stack.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

        return root1

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(N) (N is the number of overlapped nodes), Space complexity: O(min(n,m))
# Your runtime beats 27.6 % of python3 submissions
# Your memory usage beats 47.6 % of python3 submissions (15.5 MB)

# def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#     if root1 and root2:
#         return TreeNode(
#             (root1.val + root2.val),
#             self.mergeTrees(root1.left, root2.left),
#             self.mergeTrees(root1.right, root2.right),
#         )
#     else:
#         return root1 or root2
