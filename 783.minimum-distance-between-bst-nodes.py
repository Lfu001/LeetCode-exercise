#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 2 (Recursive: sliding window)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 30.95 % of python3 submissions
# Your memory usage beats 44.44 % of python3 submissions (14 MB)
class Solution:
    def __init__(self):
        self.diff = float("inf")
        self.prev = float("-inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root:
            self.minDiffInBST(root.left)

            self.diff = min(self.diff, (root.val - self.prev))
            self.prev = root.val

            self.minDiffInBST(root.right)

        return self.diff


# @lc code=end

# Solution 1 (Recursive: convert tree to list)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 6.74 % of python3 submissions
# Your memory usage beats 44.44 % of python3 submissions (13.9 MB)

# def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#     treeVals = []
#
#     def getTreeValsInorder(root) -> None:
#         if root.left:
#             getTreeValsInorder(root.left)
#         treeVals.append(root.val)
#         if root.right:
#             getTreeValsInorder(root.right)
#
#     getTreeValsInorder(root)
#     return min(map(operator.sub, treeVals, ([float("-inf")] + treeVals)))
