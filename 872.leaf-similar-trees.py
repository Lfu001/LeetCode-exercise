#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

import itertools
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 3 (Iterative: generator)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 42.11 % of python3 submissions
# Your memory usage beats 49.6 % of python3 submissions (14 MB)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafSequenceGenerator(root: Optional[TreeNode]):
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        yield node.val
                    stack.append(node.right)
                    stack.append(node.left)

        return all(
            a == b
            for a, b in itertools.zip_longest(
                leafSequenceGenerator(root1), leafSequenceGenerator(root2)
            )
        )


# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 24.14 % of python3 submissions
# Your memory usage beats 8.51 % of python3 submissions (14 MB)

# def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#     def dfs(root: Optional[TreeNode]):
#         if not root:
#             return []
#         elif not root.left and not root.right:
#             return [root.val]
#         else:
#             return dfs(root.left) + dfs(root.right)
#
#     return dfs(root1) == dfs(root2)


# Solution 2 (Recursive: generator)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 60.67 % of python3 submissions
# Your memory usage beats 49.6 % of python3 submissions (14 MB)

# def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#     def dfsGenerator(root: Optional[TreeNode]):
#         if not root:
#             return []
#         elif not root.left and not root.right:
#             yield [root.val]
#         else:
#             yield from dfsGenerator(root.left)
#             yield from dfsGenerator(root.right)
#
#     return all(
#         a == b
#         for a, b in itertools.zip_longest(dfsGenerator(root1), dfsGenerator(root2))
#     )
