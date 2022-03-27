#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
# Solution 3 (Join slices)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 95.19 % of python3 submissions
# Your memory usage beats 63.11 % of python3 submissions (14.5 MB)
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        return "-".join(s[i:(i + k)] for i in range(0, len(s), k))[::-1]

# @lc code=end

# Solution 1 (Reverse string)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 64.31 % of python3 submissions
# Your memory usage beats 52.22 % of python3 submissions (14.7 MB)

# def licenseKeyFormatting(self, s: str, k: int) -> str:
#     s = s.replace("-", "").upper()
#     licenseKey = []
#     group = ""
#     for i, c in enumerate(reversed(s)):
#         group += c
#         if (i + 1) % k == 0:
#             licenseKey.append(group)
#             group = ""
#     if group:
#         licenseKey.append(group)
#     return "-".join(licenseKey)[::-1]


# Solution 2 (Calculate the first group first)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 40.71 % of python3 submissions
# Your memory usage beats 74.58 % of python3 submissions (14.5 MB)

# def licenseKeyFormatting(self, s: str, k: int) -> str:
#     s = s.replace("-", "").upper()
#     licenseKey = []
#     if t := len(s) % k:
#         licenseKey.append(s[:t])
#     group = ""
#     for i in range(t, len(s)):
#         group += s[i]
#         if (i - t + 1) % k == 0:
#             licenseKey.append(group)
#             group = ""
#     return "-".join(licenseKey)
