#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 2 (Convert to string and search substring)
# Time complexity: O(nm), Space complexity: O(n+m)
# Your runtime beats 91.43 % of python3 submissions
# Your memory usage beats 15.1 % of python3 submissions (15.3 MB)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def toString(root):
            if not root:
                return ",#"
            else:
                return "," + str(root.val) + toString(root.left) + toString(root.right)

        return toString(subRoot) in toString(root)

# @lc code=end

# Solution 1 (Greedy)
# Time complexity: O(nm), Space complexity: O(n)
# Your runtime beats 27.23 % of python3 submissions
# Your memory usage beats 65.9 % of python3 submissions (15 MB)

# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not root:
#             return False
#         if self.isSameTree(root, subRoot):
#             return True
#         else:
#             return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
#
#     def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
#         if not s and not t:
#             return True
#         elif not s or not t:
#             return False
#         else:
#             if s.val != t.val:
#                 return False
#             else:
#                 return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
