#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 3 (Set and sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 88.45 % of python3 submissions
# Your memory usage beats 97.81 % of python3 submissions (13.8 MB)
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        treeValueSet = set()

        def dfs(root: Optional[TreeNode]):
            if root:
                treeValueSet.add(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        if len(treeValueSet) == 1:
            return -1
        else:
            treeValueList = list(treeValueSet)
            treeValueList.sort()
            return treeValueList[1]

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 85.26 % of python3 submissions
# Your memory usage beats 69.92 % of python3 submissions (13.9 MB)

# def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
#     self.ans = float("inf")
#     minNodeValInTree = root.val
#
#     def dfs(root: Optional[TreeNode]):
#         if root:
#             if minNodeValInTree < root.val < self.ans:
#                 self.ans = root.val
#             elif root.val == minNodeValInTree:
#                 dfs(root.left)
#                 dfs(root.right)
#
#     dfs(root)
#     return self.ans if self.ans < float("inf") else -1


# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 94.22 % of python3 submissions
# Your memory usage beats 17.08 % of python3 submissions (13.9 MB)

# def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
#     ans = float("inf")
#     minNodeValInTree = root.val
#
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node:
#             if minNodeValInTree < node.val < ans:
#                 ans = node.val
#             elif root.val == minNodeValInTree:
#                 stack.append(node.right)
#                 stack.append(node.left)
#
#     return ans if ans < float("inf") else -1
