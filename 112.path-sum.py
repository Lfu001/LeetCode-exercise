#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, (targetSum - root.val)) or self.hasPathSum(root.right, (targetSum - root.val))

# @lc code=end

# Solution 1
# if not root:
#     return False

# parents = [(root, 0)]
# children = []

# for _ in range(5000):
#     while parents:
#         node, pathSum = parents.pop()
#         if not node:
#             continue

#         # In case 0 <= Node.val
#         # if abs(pathSum) <= abs(targetSum):
#         #     children.append((node.left, pathSum))
#         #     children.append((node.right, pathSum))

#         pathSum += node.val
#         children.append((node.left, pathSum))
#         children.append((node.right, pathSum))

#         if (pathSum == targetSum) and not node.left and not node.right:
#             return True

#     parents = children
#     children = []

# return False
