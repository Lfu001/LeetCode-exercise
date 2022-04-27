#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

from typing import List


# @lc code=start
# Solution 1 (Count continuous 1s)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 92.23 % of python3 submissions
# Your memory usage beats 82.31 % of python3 submissions (13.8 MB)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ans = True
        for bit in bits[-2::-1]:
            if bit == 1:
                ans = not ans
            else:
                break
        return ans


# @lc code=end
