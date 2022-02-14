#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2

        x1 = list1
        x2 = list2
        head = list1 if list1.val <= list2.val else list2
        f = head

        while not (x1 is None and x2 is None):
            if x1 is None or x2 is None:
                break

            if f is x1:
                tmp = x1.next
                x1.next = x2 if x1.next is None else (x1.next if x1.next.val <= x2.val else x2)
                f = x1.next
                x1 = tmp
            else:
                tmp = x2.next
                x2.next = x1 if x2.next is None else (x1 if x1.val <= x2.next.val else x2.next)
                f = x2.next
                x2 = tmp

        return head

# @lc code=end

# Solution 1
# if list1 is None:
#     return list2
# elif list2 is None:
#     return list1

# if list1.val <= list2.val:
#     list1.next = self.mergeTwoLists(list1.next, list2)
#     return list1
# else:
#     list2.next = self.mergeTwoLists(list1, list2.next)
#     return list2


# Solution 2
# if not list1 or not list2:
#     return list1 if not list2 else list2

# x1 = list1
# x2 = list2
# head = list1 if list1.val <= list2.val else list2

# while not (x1 is None and x2 is None):
#     if x1 is None or x2 is None:
#         break

#     if x1.val <= x2.val:
#         tmp = x1.next
#         x1.next = x2 if x1.next is None else (x1.next if x1.next.val <= x2.val else x2)
#         x1 = tmp
#     else:
#         tmp = x2.next
#         x2.next = x1 if x2.next is None else (x1 if x1.val <= x2.next.val else x2.next)
#         x2 = tmp

# return head
