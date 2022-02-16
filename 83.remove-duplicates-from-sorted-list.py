#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1 = p2 = head
        while p2:
            if p2.val != p1.val:
                p1 = p1.next
                p1.val = p2.val
            p2 = p2.next
        p1.next = None
        return head

# @lc code=end
