#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 19.68 % of python3 submissions
# Your memory usage beats 46.33 % of python3 submissions (16.3 MB)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def searchDiameter(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            else:
                left = searchDiameter(root.left) + 1
                right = searchDiameter(root.right) + 1
                self.diameter = max(self.diameter, (left + right))
                return max(left, right)

        searchDiameter(root)
        return self.diameter


# @lc code=end
