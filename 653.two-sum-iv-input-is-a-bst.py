#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Solution 4 (Iterative version of Solution 3)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 84.73 % of python3 submissions
# Your memory usage beats 96.48 % of python3 submissions (16.3 MB)
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        bfsStack = [root]
        seen = set()

        for node in bfsStack:
            if (k - node.val) in seen:
                return True
            seen.add(node.val)
            if node.left:
                bfsStack.append(node.left)
            if node.right:
                bfsStack.append(node.right)

        return False

# @lc code=end

# Solution 1 (Brute force)
# Time complexity: O(n^2), Space complexity: O(n)
# Your runtime beats 5.16 % of python3 submissions
# Your memory usage beats 5.76 % of python3 submissions (20.5 MB)

# def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#     def dfs(root: Optional[TreeNode]):
#         if not root:
#             return []
#         else:
#             return dfs(root.left) + [root.val] + dfs(root.right)
#
#     nums = dfs(root)
#     return any(sum(c) == k for c in combinations(nums, 2))


# Solution 2 (Two pointers)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 49.89 % of python3 submissions
# Your memory usage beats 9.43 % of python3 submissions (20.3 MB)

# def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#     def dfs(root: Optional[TreeNode]):
#         if not root:
#             return []
#         else:
#             return dfs(root.left) + [root.val] + dfs(root.right)
#
#     nums = dfs(root)
#     i = 0
#     j = len(nums) - 1
#
#     while i < j:
#         twoSum = nums[i] + nums[j]
#         if twoSum <= k:
#             if twoSum == k:
#                 return True
#             else:
#                 i += 1
#         else:
#             j -= 1
#
#     return False


# Solution 3 (Hash table: set)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 85.18 % of python3 submissions
# Your memory usage beats 68.36 % of python3 submissions (18.1 MB)

# def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#     def dfs(root: Optional[TreeNode], k: int, seen: set):
#         if not root:
#             return False
#         if (k - root.val) in seen:
#             return True
#         seen.add(root.val)
#         return dfs(root.left, k, seen) or dfs(root.right, k, seen)
#
#     return dfs(root, k, set())
