#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
# Solution 3 (Brush up solution 1)
# Your runtime beats 66.55 % of python3 submissions
# Your memory usage beats 94.67 % of python3 submissions (13.8 MB)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False

        patternToWord = dict()

        for p, word in zip(pattern, s.split()):
            if p not in patternToWord:
                patternToWord[p] = word
            elif p in patternToWord and patternToWord[p] != word:
                return False

        return True

# @lc code=end

# Solution 1 (Hash table)
# Your runtime beats 48.85 % of python3 submissions
# Your memory usage beats 94.67 % of python3 submissions (13.9 MB)

# def wordPattern(self, pattern: str, s: str) -> bool:
#     if len(pattern) != len(s.split()):
#         return False
#
#     patternToWord = dict()
#     wordToPattern = dict()
#
#     for p, word in zip(pattern, s.split()):
#         if p not in patternToWord and word not in wordToPattern:
#             patternToWord[p] = word
#             wordToPattern[word] = p
#         else:
#             if p in patternToWord and patternToWord[p] != word:
#                 return False
#             if word in wordToPattern and wordToPattern[word] != p:
#                 return False
#
#     return True


# Solution 2
# Your runtime beats 30.68 % of python3 submissions
# Your memory usage beats 94.67 % of python3 submissions (13.9 MB)

# def wordPattern(self, pattern: str, s: str) -> bool:
#     words = s.split()
#     return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))) and len(pattern) == len(words)
