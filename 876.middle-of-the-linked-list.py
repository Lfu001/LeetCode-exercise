#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Solution 2 (Count length)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 65.96 % of python3 submissions
# Your memory usage beats 56.3 % of python3 submissions (13.8 MB)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        node = head
        for _ in range(count // 2):
            node = node.next
        return node


# @lc code=end

# Solution 1 (Two pointers)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 75.31 % of python3 submissions
# Your memory usage beats 95.71 % of python3 submissions (13.8 MB)

# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     walker = runner = head
#     while runner and runner.next:
#         walker = walker.next
#         runner = runner.next.next
#     return walker
