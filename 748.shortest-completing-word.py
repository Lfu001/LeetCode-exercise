#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

from collections import Counter
from typing import List


# @lc code=start
# Solution 2 (Intersection of collections.Counter)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 18.59 % of python3 submissions
# Your memory usage beats 97.53 % of python3 submissions (14 MB)
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = Counter(filter(str.isalpha, licensePlate.lower()))
        return min([w for w in words if Counter(w) & counter == counter], key=len)


# @lc code=end

# Solution 1 (Count: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 42.27 % of python3 submissions
# Your memory usage beats 19.08 % of python3 submissions (14.2 MB)

# def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#     counter = Counter([c.lower() for c in licensePlate if "a" <= c.lower() <= "z"])
#     shortest = " " * 16
#     for w in words:
#         wc = Counter(w)
#         if (len(w) < len(shortest)) and all(
#             wc.get(key, 0) and wc[key] >= val for key, val in counter.items()
#         ):
#             shortest = w
#     return shortest
