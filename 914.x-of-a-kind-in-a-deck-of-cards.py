#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

import math
from collections import Counter
from typing import List


# @lc code=start
# Solution 1 (GCD)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 37.15 % of python3 submissions
# Your memory usage beats 95.68 % of python3 submissions (14.1 MB)
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*Counter(deck).values()) >= 2


# @lc code=end
