#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Your runtime beats 66.35 % of python3 submissions
# Your memory usage beats 84.88 % of python3 submissions (13.8 MB)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return ans

# @lc code=end

# Solution 1
# Your runtime beats 28.72 % of python3 submissions
# Your memory usage beats 98.82 % of python3 submissions (13.7 MB)

# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     if not root:
#         return []
#     else:
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# Solution 2
# Your runtime beats 51.91 % of python3 submissions
# Your memory usage beats 63.19 % of python3 submissions (13.9 MB)

# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     ans = []
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if not node:
#             continue
#         ans.append(node.val)
#         stack.append(node.left)
#         stack.append(node.right)
#     return ans[::-1]
