#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Your runtime beats 40.7 % of python3 submissions
# Your memory usage beats 23.93 % of python3 submissions (17.9 MB)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        currentNode = dummyHead

        while currentNode.next:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

        return dummyHead.next

# @lc code=end

# Solution 1
# Your runtime beats 52.35 % of python3 submissions
# Your memory usage beats 44.17 % of python3 submissions (17.8 MB)

# def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#     while head and head.val == val:
#         head = head.next

#     if head:
#         p = head
#         while p.next:
#             if p.next.val == val:
#                 p.next = p.next.next
#             else:
#                 p = p.next

#     return head
