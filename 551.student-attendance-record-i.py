#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

import re


# @lc code=start
# Solution 3 (Regex)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 46.73 % of python3 submissions
# Your memory usage beats 61.78 % of python3 submissions (13.9 MB)
class Solution:
    def checkRecord(self, s: str) -> bool:
        return not bool(re.compile("A.*A|LLL").search(s))

# @lc code=end

# Solution 1 (Traverse and count)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 74.11 % of python3 submissions
# Your memory usage beats 12.92 % of python3 submissions (14.1 MB)

# def checkRecord(self, s: str) -> bool:
#     attendanceRecordCount = {"A": 0, "L": 0}
#     for c in s:
#         if c != "P":
#             attendanceRecordCount[c] += 1
#             if attendanceRecordCount["A"] >= 2 or attendanceRecordCount["L"] >= 3:
#                 return False
#         if c != "L":
#             attendanceRecordCount["L"] = 0
#     return True


# Solution 2 (Built-in function: str.count and in)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 46.73 % of python3 submissions
# Your memory usage beats 61.78 % of python3 submissions (13.8 MB)

# def checkRecord(self, s: str) -> bool:
#     return (s.count("A") < 2) and ("LLL" not in s)
