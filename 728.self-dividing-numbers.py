#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

from typing import List


# @lc code=start
# Solution 1 (Brute force)
# Time complexity: O(len(Integer[left:right])), Space complexity: O(1)
# Your runtime beats 53.02 % of python3 submissions
# Your memory usage beats 75.65 % of python3 submissions (13.8 MB)
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, (right + 1)):
            if all(int(digit) and (i % int(digit) == 0) for digit in str(i)):
                ans.append(i)
        return ans


# @lc code=end
