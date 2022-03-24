#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
# Solution 2 (s in rotation of s)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 94.1 % of python3 submissions
# Your memory usage beats 65.03 % of python3 submissions (14 MB)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

# @lc code=end

# Solution 1 (Greedy)
# Time complexity: O(n^2), Space complexity: O(1)
# Your runtime beats 38.76 % of python3 submissions
# Your memory usage beats 92.73 % of python3 submissions (13.9 MB)

# def repeatedSubstringPattern(self, s: str) -> bool:
#     substringLength = 1
#     sLength = len(s)
#
#     while substringLength <= sLength // 2:
#         q, r = divmod(sLength, substringLength)
#         if r == 0 and s[:substringLength] * q == s:
#             return True
#         substringLength += 1
#
#     return False
