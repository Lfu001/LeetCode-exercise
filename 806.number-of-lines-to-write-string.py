#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

from typing import List


# @lc code=start
# Solution 1 (Simulation)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 91.82 % of python3 submissions
# Your memory usage beats 18.66 % of python3 submissions (13.9 MB)
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        numOfLines = 1
        lineWidth = 0
        for c in s:
            letterWidth = widths[ord(c) - ord("a")]
            if (lineWidth + letterWidth) > 100:
                numOfLines += 1
                lineWidth = 0
            lineWidth += letterWidth
        return [numOfLines, lineWidth]


# @lc code=end
