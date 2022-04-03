#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
# Solution 1 (Recursive)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 35.79 % of python3 submissions
# Your memory usage beats 22.46 % of python3 submissions (14.2 MB)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        return s[:k][::-1] + s[k:(2 * k)] + self.reverseStr(s[(2 * k):], k)

# @lc code=end

# Solution 1 (Slice)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 49.07 % of python3 submissions
# Your memory usage beats 61.48 % of python3 submissions (14.1 MB)

# def reverseStr(self, s: str, k: int) -> str:
#     if len(s) < k:
#         return s[::-1]
#     elif len(s) < 2 * k:
#         return s[:k][::-1] + s[k:]
#     else:
#         reversedStr = ""
#         reverseFlag = False
#         for i in range(0, len(s), k):
#             reversedStr += s[i:(i + k)] if reverseFlag else s[i:(i + k)][::-1]
#             reverseFlag ^= True
#         return reversedStr


# Solution 2 (Slice: optimized)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 29.02 % of python3 submissions
# Your memory usage beats 61.48 % of python3 submissions (14.1 MB)

# def reverseStr(self, s: str, k: int) -> str:
#     reversedStr = ""
#     reverseFlag = False
#     for i in range(0, len(s), k):
#         reversedStr += s[i:(i + k)] if reverseFlag else s[i:(i + k)][::-1]
#         reverseFlag ^= True
#     return reversedStr

sol = Solution()
sol.reverseStr("abcdefg", 2)
