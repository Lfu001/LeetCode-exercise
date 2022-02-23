#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Your runtime beats 70.84 % of python3 submissions
# Your memory usage beats 22.65 % of python3 submissions (29.8 MB)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa

# @lc code=end
