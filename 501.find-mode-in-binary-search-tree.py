#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 2 (Recursive)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 29.74 % of python3 submissions
# Your memory usage beats 91.53 % of python3 submissions (18 MB)
class Solution:
    def __init__(self) -> None:
        self._currentVal = None
        self._currentCount = 0
        self._maxCount = 0
        self._modeCount = 0
        self._modes = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self._inorder(root)
        self._modes = [None] * self._modeCount
        self._modeCount = 0
        self._currentCount = 0
        self._inorder(root)
        return self._modes

    def _handleValue(self, val):
        if val != self._currentVal:
            self._currentVal = val
            self._currentCount = 0
        self._currentCount += 1
        if self._currentCount > self._maxCount:
            self._maxCount = self._currentCount
            self._modeCount = 1
        elif self._currentCount == self._maxCount:
            if self._modes:
                self._modes[self._modeCount] = self._currentVal
            self._modeCount += 1

    def _inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self._inorder(root.left)
        self._handleValue(root.val)
        self._inorder(root.right)

# @lc code=end

# Solution 1 (Iterative: using collections.Counter)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 93.12 % of python3 submissions
# Your memory usage beats 43.45 % of python3 submissions (18.5 MB)

# def findMode(self, root: Optional[TreeNode]) -> List[int]:
#     frequency = Counter()
#     stack = [root]
#
#     while stack:
#         node = stack.pop()
#         if not node:
#             continue
#         stack.append(node.right)
#         stack.append(node.left)
#         frequency[node.val] += 1
#
#     maxFrequency = max(frequency.values())
#
#     return [key for key, val in frequency.items() if val == maxFrequency]


tree = TreeNode(6, TreeNode(2, TreeNode(2), None), TreeNode(10, TreeNode(10), None))
sol = Solution()
ans = sol.findMode(tree)
print(ans)
