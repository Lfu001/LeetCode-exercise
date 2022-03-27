#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
# Solution 1 (Search from √(area) to 1 in sequence)
# Time complexity: O(√(n)), Space complexity: O(1)
# Your runtime beats 32.91 % of python3 submissions
# Your memory usage beats 16.22 % of python3 submissions (13.9 MB)
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [(area // i), i]

# @lc code=end
