#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
import re
from typing import List


# @lc code=start
# Solution 2 (Regular expression: using filter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 71.44 % of python3 submissions
# Your memory usage beats 20.49 % of python3 submissions (13.9 MB)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(filter(re.compile("(?i)^([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$").match, words))

# @lc code=end

# Solution 1 (Using set.issubset)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 69.8 % of python3 submissions
# Your memory usage beats 72.45 % of python3 submissions (13.8 MB)

# def findWords(self, words: List[str]) -> List[str]:
#     keyboard = [
#         {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"},
#         {"a", "s", "d", "f", "g", "h", "j", "k", "l"},
#         {"z", "x", "c", "v", "b", "n", "m"},
#     ]
#
#     ans = []
#
#     for word in words:
#         wordSet = set(word.lower())
#         if any(map(wordSet.issubset, keyboard)):
#             ans.append(word)
#
#     return ans
