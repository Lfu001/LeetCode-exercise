#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            minDepthLeft = self.minDepth(root.left)
            minDepthRight = self.minDepth(root.right)
            return (min(minDepthLeft, minDepthRight) or max(minDepthLeft, minDepthRight)) + 1

# @lc code=end

# Solution 1
# if not root:
#     return 0

# depth = 0
# parents = [root]
# children = []

# for _ in range(100000):
#     depth += 1
#     while parents:
#         node = parents.pop()
#         if not node:
#             continue
#         if not node.left and not node.right:
#             return depth
#         else:
#             children.append(node.left)
#             children.append(node.right)
#     parents = children
#     children = []

# return depth
