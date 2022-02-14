#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# @lc code=end

# Solution 1
# len_haystack = len(haystack)
# len_needle = len(needle)

# if not needle:
#     return 0
# if len_haystack < len_needle:
#     return -1

# for i in range(len_haystack - len_needle + 1):
#     if haystack[i:i + len_needle] == needle:
#         return i

# return -1


# Solution 2
# if not needle:
#     return 0
# elif len(haystack) < len(needle) or needle not in haystack:
#     return -1
# else:
#     return haystack.index(needle)
