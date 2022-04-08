#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
# Solution 2 (Iterative)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 56.58 % of python3 submissions
# Your memory usage beats 82.46 % of python3 submissions (16 MB)
class Solution:
    def preorder(self, root: "Node") -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            stack += node.children[::-1]
        return ans

# @lc code=end

# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 56.58 % of python3 submissions
# Your memory usage beats 17.12 % of python3 submissions (16.3 MB)

# def preorder(self, root: "Node") -> List[int]:
#     if not root:
#         return []
#     else:
#         return [root.val] + sum((self.preorder(child) for child in root.children), start=[])
