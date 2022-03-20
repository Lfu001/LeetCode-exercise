#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 3 (Morris traversal)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 33.6 % of python3 submissions
# Your memory usage beats 92.96 % of python3 submissions (14.1 MB)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_ = 0
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                else:
                    prev.right = None
                    if prev == root.left and not prev.left:
                        sum_ += prev.val
                    root = root.right
            else:
                root = root.right
        return sum_

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 82.86 % of python3 submissions
# Your memory usage beats 6.04 % of python3 submissions (14.9 MB)

# def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#     def helper(root, whichChild):
#         if not root:
#             return 0
#         elif not root.left and not root.right:
#             return root.val if whichChild == "left" else 0
#         return helper(root.left, "left") + helper(root.right, "right")

#     return helper(root, None)


# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 14.64 % of python3 submissions
# Your memory usage beats 92.96 % of python3 submissions (14.2 MB)

# def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#     seen = [(root, None)]
#     sum_ = 0
#     while seen:
#         node, whichChild = seen.pop()
#         if node:
#             seen.append((node.right, "right"))
#             seen.append((node.left, "left"))
#             if not node.left and not node.right and whichChild == "left":
#                 sum_ += node.val
#     return sum_
