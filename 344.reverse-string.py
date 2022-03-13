#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
# Solution 3 (Mirror)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 98.19 % of python3 submissions
# Your memory usage beats 91.62 % of python3 submissions (18.3 MB)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]

# @lc code=end

# Solution 1 (Two pointers: Loop)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 38.54 % of python3 submissions
# Your memory usage beats 34.98 % of python3 submissions (18.5 MB)

# def reverseString(self, s: List[str]) -> None:
#     """
#     Do not return anything, modify s in-place instead.
#     """
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1


# Solution 2 (Two pointers: Recursion)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 59.44 % of python3 submissions
# Your memory usage beats 5.77 % of python3 submissions (43.3 MB)

# def reverseString(self, s: List[str]) -> None:
#     def helper(s: List[str], left: int, right: int) -> None:
#         if left < right:
#             s[left], s[right] = s[right], s[left]
#             helper(s, (left + 1), (right - 1))
#
#     helper(s, 0, (len(s) - 1))
