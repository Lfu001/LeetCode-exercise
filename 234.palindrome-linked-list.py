#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Your runtime beats 66.14 % of python3 submissions
# Your memory usage beats 34.7 % of python3 submissions (47 MB)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        runner = walker = head
        prev = None

        while runner and runner.next:
            runner = runner.next.next
            walker.next, walker, prev = prev, walker.next, walker

        runner = walker.next if runner else walker
        palindrome = True

        while runner:
            if runner.val != prev.val:
                palindrome = False
            runner = runner.next
            prev.next, prev, walker = walker, prev.next, prev

        return palindrome

# @lc code=end

# Solution 1
# Your runtime beats 38.92 % of python3 submissions
# Your memory usage beats 50.07 % of python3 submissions (46.6 MB)

# def isPalindrome(self, head: Optional[ListNode]) -> bool:
#     nums = list()
#     while head:
#         nums.append(head.val)
#         head = head.next
#     return nums == nums[::-1]
