#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Your runtime beats 69.18 % of python3 submissions
# Your memory usage beats 10.71 % of python3 submissions (20.4 MB)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lastNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return lastNode

# @lc code=end

# Solution 1
# Your runtime beats 11.43 % of python3 submissions
# Your memory usage beats 54.2 % of python3 submissions (15.6 MB)

# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     prevNode = None
#     currentNode = head
#     while currentNode:
#         currentNode.next, currentNode, prevNode = prevNode, currentNode.next, currentNode
#     return prevNode
