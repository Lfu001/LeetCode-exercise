#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter


# Solution 3 (Hash table: count the number of odds)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 15.95 % of python3 submissions
# Your memory usage beats 74.27 % of python3 submissions (13.9 MB)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        numOfOdds = sum(numOfLetter & 1 for numOfLetter in Counter(s).values())
        return len(s) - numOfOdds + bool(numOfOdds)

# @lc code=end

# Solution 1 (Hash table: dict)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 9.47 % of python3 submissions
# Your memory usage beats 33.61 % of python3 submissions (13.9 MB)

# def longestPalindrome(self, s: str) -> int:
#     letters = dict()
#
#     for c in s:
#         if c not in letters:
#             letters[c] = 0
#         letters[c] += 1
#
#     ans = sum(numOfLetter >> 1 << 1 for numOfLetter in letters.values())
#
#     if any(numOfLetter & 1 == 1 for numOfLetter in letters.values()):
#         ans += 1
#
#     return ans


# Solution 2 (Hash table: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 40.74 % of python3 submissions
# Your memory usage beats 33.61 % of python3 submissions (13.9 MB)

# def longestPalindrome(self, s: str) -> int:
#     letters = Counter(s)
#
#     ans = sum(numOfLetter >> 1 << 1 for numOfLetter in letters.values())
#
#     if any(numOfLetter & 1 == 1 for numOfLetter in letters.values()):
#         ans += 1
#
#     return ans
