#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            center = (left + right) // 2
            root = TreeNode(nums[center])
            root.left = buildBST(left, (center - 1))
            root.right = buildBST((center + 1), right)
            return root

        return buildBST(0, (len(nums) - 1))

# @lc code=end

# Solution 1
# if not nums:
#     return None
# center = len(nums) // 2
# return TreeNode(nums[center], self.sortedArrayToBST(nums[:center]), self.sortedArrayToBST(nums[(center + 1):]))


# Solution 2
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     return self.buildBST(nums, 0, (len(nums) - 1))

# def buildBST(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
#     if left > right:
#         return None
#     center = (left + right) // 2
#     return TreeNode(nums[center], self.buildBST(nums, left, (center - 1)), self.buildBST(nums, (center + 1), right))
