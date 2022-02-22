#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Your runtime beats 84.68 % of python3 submissions
# Your memory usage beats 77.51 % of python3 submissions (17.5 MB)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = runner = head

        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker is runner:
                return True

        return False

# @lc code=end

# Solution 1
# Your runtime beats 48.39 % of python3 submissions
# Your memory usage beats 77.51 % of python3 submissions (17.5 MB)

# def hasCycle(self, head: Optional[ListNode]) -> bool:
#     for _ in range(10001):
#         if not head:
#             return False
#         head = head.next
#     return True
