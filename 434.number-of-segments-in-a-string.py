#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
# Solution 3 (Iterate and count: add dummy space)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 22.12 % of python3 submissions
# Your memory usage beats 59.68 % of python3 submissions (13.8 MB)
class Solution:
    def countSegments(self, s: str) -> int:
        s = list(s) + [" "]
        segmentCount = 0
        for i in range(1, len(s)):
            if s[i] == " " != s[i - 1]:
                segmentCount += 1
        return segmentCount

# @lc code=end

# Solution 1 (Using built-in functions: str.split and len)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 36.71 % of python3 submissions
# Your memory usage beats 59.68 % of python3 submissions (13.8 MB)

# def countSegments(self, s: str) -> int:
#     return len(s.split())


# Solution 2 (Iterate and count)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 70.35 % of python3 submissions
# Your memory usage beats 19.51 % of python3 submissions (13.9 MB)

# def countSegments(self, s: str) -> int:
#     segmentCount = 0
#     for i in range(len(s)):
#         if (i == 0 or s[i - 1] == " ") and s[i] != " ":
#             segmentCount += 1
#     return segmentCount
