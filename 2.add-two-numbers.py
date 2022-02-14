#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        for p in [l1, l2]:
            i = 0
            while p is not None:
                sum_ += p.val * (10 ** i)
                p = p.next
                i += 1

        p = None
        for i in (int(c) for c in str(sum_)):
            p = ListNode(i, p)

        return p

# @lc code=end
