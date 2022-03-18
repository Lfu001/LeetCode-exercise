#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
# Solution 2 (Count)
# Time complexity: O(n^2) , Space complexity: O(1)
# Note: This approach is O(n^2) but fast because `set()` and `count()` are implemented in C.
# Your runtime beats 73.12 % of python3 submissions
# Your memory usage beats 63.08 % of python3 submissions (14.2 MB)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False

        return True

# @lc code=end

# Solution 1 (Hash map)
# Time complexity: O(n+m)≒O(n) , Space complexity: O(m)
# (∵ checking length first (if n > m -> false))
# Your runtime beats 14.83 % of python3 submissions
# Your memory usage beats 63.08 % of python3 submissions (14.2 MB)

# def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#     if len(ransomNote) > len(magazine):
#         return False
#
#     availableLetters = dict()
#
#     for letter in magazine:
#         if letter not in availableLetters:
#             availableLetters[letter] = 0
#         availableLetters[letter] += 1
#
#     for letter in ransomNote:
#         if letter not in availableLetters or availableLetters[letter] == 0:
#             return False
#         availableLetters[letter] -= 1
#
#     return True
