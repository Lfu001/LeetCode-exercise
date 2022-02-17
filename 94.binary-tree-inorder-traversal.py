#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        while root:
            if not root.left:
                ans.append(root.val)
                root = root.right
            else:
                p = root.left
                while p.right:
                    p = p.right
                p.right = root
                tmp = root
                root = root.left
                tmp.left = None
        return ans

# @lc code=end

# Solution 1
# if not root:
#     return []
# else:
#     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Solution 2
# ans = list()
# stack = list()

# while root or stack:
#     while root:
#         stack.append(root)
#         root = root.left
#     root = stack.pop()
#     ans.append(root.val)
#     root = root.right

# return ans
