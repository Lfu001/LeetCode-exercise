#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        length_ = 0
        while s[p] == " ":
            p -= 1
        while s[p] != " " and p >= 0:
            p -= 1
            length_ += 1
        return length_

# @lc code=end

# Solution 1
# return len(s.split()[-1])
