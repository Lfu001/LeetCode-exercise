#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 2 (BFS: simplified)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 95.43 % of python3 submissions
# Your memory usage beats 89.61 % of python3 submissions (16.4 MB)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        level = [root]
        while level:
            ans.append(sum(node.val for node in level) / len(level))
            level = [child for node in level for child in (node.left, node.right) if child]
        return ans

# @lc code=end

# Solution 1 (BFS)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 76.06 % of python3 submissions
# Your memory usage beats 47.8 % of python3 submissions (16.6 MB)

# def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#     ans = []
#     currentLevel = [root]
#     while any(currentLevel):
#         nextLevel = []
#         numOfNodesInCurrentLevel = 0
#         sumOfNodeValsOfCurrentLevel = 0
#         for _ in range(len(currentLevel)):
#             node = currentLevel.pop()
#             if node:
#                 numOfNodesInCurrentLevel += 1
#                 sumOfNodeValsOfCurrentLevel += node.val
#                 nextLevel.append(node.left)
#                 nextLevel.append(node.right)
#         ans.append(sumOfNodeValsOfCurrentLevel / numOfNodesInCurrentLevel)
#         currentLevel = nextLevel
#     return ans
