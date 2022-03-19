#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter


# Solution 2 (Hash table: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 56.4 % of python3 submissions
# Your memory usage beats 32.75 % of python3 submissions (14.2 MB)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordCount = Counter(s)
        for i, c in enumerate(s):
            if wordCount[c] == 1:
                return i
        return -1

# @lc code=end

# Solution 1 (Hash table)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 29.1 % of python3 submissions
# Your memory usage beats 32.75 % of python3 submissions (14.2 MB)

# def firstUniqChar(self, s: str) -> int:
#     word_count = dict()
#     for i, c in enumerate(s):
#         if c not in word_count:
#             word_count[c] = [i, 0]
#         word_count[c][1] += 1
#     try:
#         return next(v[0] for _, v in word_count.items() if v[1] == 1)
#     except StopIteration:
#         return -1
