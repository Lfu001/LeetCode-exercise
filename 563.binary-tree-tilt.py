#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 1 (Recursive: post order)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 28.98 % of python3 submissions
# Your memory usage beats 13.16 % of python3 submissions (16.5 MB)
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def getSumOfTilt(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return (0, 0)
            sumOfLeftSubtreeValues, sumOfLeftSubtreeTilt = getSumOfTilt(root.left)
            sumOfRightSubtreeValues, sumOfRightSubtreeTilt = getSumOfTilt(root.right)
            sumOfThisSubtreeValues = root.val + sumOfLeftSubtreeValues + sumOfRightSubtreeValues
            tilt = abs(sumOfLeftSubtreeValues - sumOfRightSubtreeValues)
            sumOfThisSubtreeTilt = tilt + sumOfLeftSubtreeTilt + sumOfRightSubtreeTilt
            return (sumOfThisSubtreeValues, sumOfThisSubtreeTilt)

        _, sumOfTilt = getSumOfTilt(root)
        return sumOfTilt

# @lc code=end
