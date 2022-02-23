#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Your runtime beats 53.95 % of python3 submissions
# Your memory usage beats 84.93 % of python3 submissions (13.9 MB)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 53.95 % of python3 submissions
# Your memory usage beats 98.61 % of python3 submissions (13.8 MB)

# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     if not root:
#         return []
#     else:
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
