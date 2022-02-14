#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]
        index = 0

        for matching in (len(set(list(x))) == 1 for x in zip(*strs)):
            if not matching:
                return strs[0][:index]
            index += 1

        return strs[0][:index]

# @lc code=end
