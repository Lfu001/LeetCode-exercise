#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s) - 1):
            ans += (-1) ** (romanNumerals[s[i]] < romanNumerals[s[i + 1]]) * romanNumerals[s[i]]
        return ans + romanNumerals[s[-1]]

# @lc code=end

# Solution 1
# romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# romanNumeralsUsingSubtraction = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
# sumOfRomanNumerals = 0

# for k in romanNumeralsUsingSubtraction:
#     if k in s:
#         sumOfRomanNumerals += romanNumeralsUsingSubtraction[k]
#         s = s.replace(k, "")

# for c in s:
#     sumOfRomanNumerals += romanNumerals[c]

# return sumOfRomanNumerals
