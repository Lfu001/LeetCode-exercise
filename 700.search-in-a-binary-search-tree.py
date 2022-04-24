#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 4 (Iterative: optimized for BST)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 42.52 % of python3 submissions
# Your memory usage beats 63.76 % of python3 submissions (16.5 MB)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                break
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return node


# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 42.52 % of python3 submissions
# Your memory usage beats 63.76 % of python3 submissions (16.5 MB)

# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#     if not root or root.val == val:
#         return root
#     else:
#         return self.searchBST(root.left, val) or self.searchBST(root.right, val)


# Solution 2 (Recursive: optimized for BST)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 21.89 % of python3 submissions
# Your memory usage beats 18.88 % of python3 submissions (16.7 MB)

# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#     if not root or root.val == val:
#         return root
#     elif root.val > val:
#         return self.searchBST(root.left, val)
#     else:
#         return self.searchBST(root.right, val)


# Solution 3 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 24.76 % of python3 submissions
# Your memory usage beats 18.88 % of python3 submissions (16.6 MB)

# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node:
#             if node.val == val:
#                 return node
#             else:
#                 stack.append(node.right)
#                 stack.append(node.left)
#     return None
