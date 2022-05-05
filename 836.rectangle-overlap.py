#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

from typing import List


# @lc code=start
# Solution 1 (Not not overlap)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 5.08 % of python3 submissions
# Your memory usage beats 68.19 % of python3 submissions (13.8 MB)
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            (rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
            or (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        )


# @lc code=end
