#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
# Solution 2 (Two pointers: avoid loop-in-loop)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 21.37 % of python3 submissions
# Your memory usage beats 43.56 % of python3 submissions (15.1 MB)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in vowels:
                    left += 1
                if s[right] not in vowels:
                    right -= 1

        return "".join(s)

# @lc code=end

# Solution 1 (Two pointers)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 83.36 % of python3 submissions
# Your memory usage beats 64.7 % of python3 submissions (15.1 MB)

# def reverseVowels(self, s: str) -> str:
#     s = list(s)
#     vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         while left < right and s[left] not in vowels:
#             left += 1
#         while left < right and s[right] not in vowels:
#             right -= 1
#
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#
#     return "".join(s)
