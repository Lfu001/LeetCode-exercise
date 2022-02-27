#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
# Your runtime beats 76.32 % of python3 submissions
# Your memory usage beats 94.26 % of python3 submissions (14.1 MB)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Approach: Using bijection
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# @lc code=end

# Solution 1
# Your runtime beats 82.81 % of python3 submissions
# Your memory usage beats 45.92 % of python3 submissions (14.4 MB)

# def isIsomorphic(self, s: str, t: str) -> bool:
#     s_to_t = dict()
#     t_from_s = dict()

#     for sc, tc in zip(s, t):
#         if sc in s_to_t:
#             if s_to_t[sc] != tc:
#                 return False
#         if tc in t_from_s:
#             if t_from_s[tc] != sc:
#                 return False
#         s_to_t[sc] = tc
#         t_from_s[tc] = sc

#     return True
