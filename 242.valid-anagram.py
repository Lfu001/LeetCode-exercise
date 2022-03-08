#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# Your runtime beats 89.64 % of python3 submissions
# Your memory usage beats 74.3 % of python3 submissions (14.5 MB)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False

        return True

# @lc code=end

# Solution 1
# Your runtime beats 53.26 % of python3 submissions
# Your memory usage beats 9.95 % of python3 submissions (15.1 MB)

# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)


# Solution 2
# Your runtime beats 56.34 % of python3 submissions
# Your memory usage beats 74.3 % of python3 submissions (14.5 MB)

# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     s_count = dict()
#     t_count = dict()
#
#     for sc, tc in zip(s, t):
#         if sc not in s_count:
#             s_count[sc] = 0
#         if tc not in t_count:
#             t_count[tc] = 0
#         s_count[sc] += 1
#         t_count[tc] += 1
#
#     return s_count == t_count


# Solution 3
# Your runtime beats 14.64 % of python3 submissions
# Your memory usage beats 96.69 % of python3 submissions (14.4 MB)


# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     count = dict()
#
#     for sc, tc in zip(s, t):
#         if sc not in count:
#             count[sc] = 0
#         if tc not in count:
#             count[tc] = 0
#         count[sc] += 1
#         count[tc] -= 1
#
#     return not any(count.values())
