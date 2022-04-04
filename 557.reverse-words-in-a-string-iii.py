#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
# Solution 3 (Reverse twice)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 82.6 % of python3 submissions
# Your memory usage beats 85.35 % of python3 submissions (14.6 MB)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]

# @lc code=end

# Solution 1 (Built-in function: str.join and str.split)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 76.65 % of python3 submissions
# Your memory usage beats 49.94 % of python3 submissions (14.7 MB)

# def reverseWords(self, s: str) -> str:
#     return " ".join(word[::-1] for word in s.split(" "))


# Solution 2 (Traverse the given string and reverse each words)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 28.81 % of python3 submissions
# Your memory usage beats 49.94 % of python3 submissions (14.7 MB)

# def reverseWords(self, s: str) -> str:
#     ans = ""
#     i = 0
#     sentenceLength = len(s)

#     while True:
#         word = ""
#         while i < sentenceLength and s[i] != " ":
#             word += s[i]
#             i += 1
#         ans += word[::-1]
#         i += 1
#         if i >= sentenceLength:
#             break
#         else:
#             ans += " "

#     return ans
