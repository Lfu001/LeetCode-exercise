#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                depthLeft = getDepth(root.left)
                if depthLeft is None:
                    return None
                depthRight = getDepth(root.right)
                if depthRight is None:
                    return None
                if abs(depthLeft - depthRight) <= 1:
                    return (max(depthLeft, depthRight) + 1)
                else:
                    return None
        return getDepth(root) is not None

# @lc code=end

# Solution 1
# def isBalanced(self, root: Optional[TreeNode]) -> bool:
#     def getDepthAndIsBalanced(root: Optional[TreeNode]) -> Tuple[int, bool]:
#         if not root:
#             return 0, True
#         else:
#             depthLeft, balanceLeft = getDepthAndIsBalanced(root.left)
#             depthRight, balanceRight = getDepthAndIsBalanced(root.right)
#             if balanceLeft and balanceRight and (abs(depthLeft - depthRight) <= 1):
#                 return (max(depthLeft, depthRight) + 1), True
#             else:
#                 return None, False
#     return getDepthAndIsBalanced(root)[1]
