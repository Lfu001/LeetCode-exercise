#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
# Solution 5 (Sum of ASCII value)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 19.04 % of python3 submissions
# Your memory usage beats 79.69 % of python3 submissions (13.8 MB)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

# @lc code=end

# Solution 1 (Bit manipulation: Traverse separately)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 22.17 % of python3 submissions
# Your memory usage beats 99.92 % of python3 submissions (13.7 MB)

# def findTheDifference(self, s: str, t: str) -> str:
#     x = 0
#     for c in s:
#         x ^= ord(c)
#     for c in t:
#         x ^= ord(c)
#     return chr(x)


# Solution 2 (Bit manipulation: Traverse simultaneously)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 87.79 % of python3 submissions
# Your memory usage beats 36.53 % of python3 submissions (14 MB)

# def findTheDifference(self, s: str, t: str) -> str:
#     x = 0
#     for cs, ts in zip(s, t):
#         x = x ^ ord(cs) ^ ord(ts)
#     x ^= ord(t[-1])
#     return chr(x)


# Solution 3 (Hash table: dict)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 32.05 % of python3 submissions
# Your memory usage beats 36.53 % of python3 submissions (14 MB)

# def findTheDifference(self, s: str, t: str) -> str:
#     wordCount = dict()
#     for cs in s:
#         if cs not in wordCount:
#             wordCount[cs] = 0
#         wordCount[cs] += 1
#     for ct in t:
#         if ct in wordCount and wordCount[ct] > 0:
#             wordCount[ct] -= 1
#         else:
#             return ct


# Solution 4 (Bit manipulation: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 27.98 % of python3 submissions
# Your memory usage beats 36.53 % of python3 submissions (14 MB)

# def findTheDifference(self, s: str, t: str) -> str:
#     wordCount = Counter(s)
#     for ct in t:
#         if ct in wordCount and wordCount[ct] > 0:
#             wordCount[ct] -= 1
#         else:
#             return ct
