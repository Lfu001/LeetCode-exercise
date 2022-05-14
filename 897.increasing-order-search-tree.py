#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


# @lc code=start
# Solution 2 (Recursive: in-place)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 8.95 % of python3 submissions
# Your memory usage beats 81.17 % of python3 submissions (13.9 MB)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(current: TreeNode, tail: TreeNode = None):
            if not current:
                return tail
            ans = inorder(current.left, current)
            current.left = None
            current.right = inorder(current.right, tail)
            return ans

        return inorder(root)


# @lc code=end

# Solution 1 (Morris Traversal)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 50.08 % of python3 submissions
# Your memory usage beats 39.71 % of python3 submissions (14 MB)

# def increasingBST(self, root: TreeNode) -> TreeNode:
#     def inorder(current: TreeNode):
#         while current:
#             if not current.left:
#                 yield current.val
#                 current = current.right
#             else:
#                 pre = current.left
#                 while pre.right and pre.right is not current:
#                     pre = pre.right
#                 if not pre.right:
#                     pre.right = current
#                     current = current.left
#                 else:
#                     pre.right = None
#                     yield current.val
#                     current = current.right
#
#     ans = TreeNode()
#     node = ans
#     for val in inorder(root):
#         node.right = TreeNode(val)
#         node = node.right
#     return ans.right
