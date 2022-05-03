#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

import re
from collections import Counter
from typing import List


# @lc code=start
# Solution 2 (Built-in max with key)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 35.37 % of python3 submissions
# Your memory usage beats 83.98 % of python3 submissions (13.9 MB)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        withoutPunctuation = re.sub("[!?',;.]", " ", paragraph.lower())
        wc = Counter(word for word in withoutPunctuation.split() if word not in banned)
        return max(wc, key=wc.get)


# @lc code=end

# Solution 1 (Sort)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 52.56 % of python3 submissions
# Your memory usage beats 40.68 % of python3 submissions (14 MB)

# def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#     wc = Counter(re.sub("[!?',;.]", " ", paragraph.lower()).split())
#     for word, _ in wc.most_common():
#         if word not in banned:
#             return word
