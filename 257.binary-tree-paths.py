#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 2 (Iterative)
# Your runtime beats 66.2 % of python3 submissions
# Your memory usage beats 55.41 % of python3 submissions (13.9 MB)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        seen = [(root, "")]
        paths = []

        while seen:
            node, pathToNode = seen.pop()
            if not node:
                continue
            if not node.left and not node.right:
                paths.append(pathToNode + str(node.val))

            seen.append((node.right, (pathToNode + str(node.val) + "->")))
            seen.append((node.left, (pathToNode + str(node.val) + "->")))

        return paths

# @lc code=end

# Solution 1 (Recursive)
# Your runtime beats 24.23 % of python3 submissions
# Your memory usage beats 98.96 % of python3 submissions (13.8 MB)

# def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#     paths = []
#     if root.left:
#         for leftPath in self.binaryTreePaths(root.left):
#             paths.append(str(root.val) + "->" + leftPath)
#     if root.right:
#         for rightPath in self.binaryTreePaths(root.right):
#             paths.append(str(root.val) + "->" + rightPath)
#     if not root.left and not root.right:
#         paths.append(str(root.val))
#     return paths
