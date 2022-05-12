#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

from collections import Counter
from typing import List


# @lc code=start
# Solution 3 (Counter and list comprehensions)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 65.44 % of python3 submissions
# Your memory usage beats 69.68 % of python3 submissions (13.8 MB)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wc = Counter(s1.split()) + Counter(s2.split())
        return [word for word in wc if wc[word] == 1]


# @lc code=end

# Solution 1 (Xor set)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 5.46 % of python3 submissions
# Your memory usage beats 69.68 % of python3 submissions (13.9 MB)

# def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#     wc1 = Counter(s1.split())
#     wc2 = Counter(s2.split())
#     notCommonWords = set(wc1) ^ set(wc2)
#     return [word for word in notCommonWords if (wc1[word] or wc2[word]) == 1]


# Solution 2 (Counter and filter)
# Time complexity: O(m+n), Space complexity: O(m+n)
# Your runtime beats 65.44 % of python3 submissions
# Your memory usage beats 20.21 % of python3 submissions (14 MB)

# def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#     wc = Counter(s1.split()) + Counter(s2.split())
#     return list(filter(lambda x: wc[x] == 1, wc))
