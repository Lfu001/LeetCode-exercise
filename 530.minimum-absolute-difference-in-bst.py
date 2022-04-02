#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 3 (Recursive: using list and helper function)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 88.11 % of python3 submissions
# Your memory usage beats 7.6 % of python3 submissions (16.4 MB)
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        treeVals = []

        def inorder(root: Optional[TreeNode]) -> None:
            if root.left:
                inorder(root.left)
            treeVals.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        return min(b - a for a, b in zip(treeVals, treeVals[1:]))

# @lc code=end

# Solution 1 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 86.19 % of python3 submissions
# Your memory usage beats 47 % of python3 submissions (16 MB)

# def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#     minAbsDiff = float("inf")
#     prevVal = float("-inf")
#     node = root
#     stack = []
#
#     while True:
#         print(list(map(lambda x: x.val, stack)))
#         if node:
#             stack.append(node)
#             node = node.left
#         elif stack:
#             node = stack.pop()
#             diff = node.val - prevVal
#             if diff < minAbsDiff:
#                 minAbsDiff = diff
#                 if minAbsDiff == 0:
#                     return minAbsDiff
#             prevVal = node.val
#             node = node.right
#         else:
#             break
#
#     return minAbsDiff


# Solution 2 (Recursive: using class member)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 79.09 % of python3 submissions
# Your memory usage beats 31.37 % of python3 submissions (16.1 MB)

# class Solution:
#     def __init__(self) -> None:
#         self.minAbsDiff = float("inf")
#         self.prevVal = float("-inf")
#
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         if root:
#             self.getMinimumDifference(root.left)
#
#             self.minAbsDiff = min(self.minAbsDiff, root.val - self.prevVal)
#             self.prevVal = root.val
#
#             self.getMinimumDifference(root.right)
#
#         return self.minAbsDiff
