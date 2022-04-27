#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
# Solution 2 (Using ord and chr)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 22.4 % of python3 submissions
# Your memory usage beats 53.85 % of python3 submissions (13.9 MB)
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        diff = ord("a") - ord("A")
        for c in s:
            if "A" <= c <= "Z":
                ans += chr(ord(c) + diff)
            else:
                ans += c
        return ans


# @lc code=end

# Solution 1 (Built-in: str.lower)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 10.47 % of python3 submissions
# Your memory usage beats 8.94 % of python3 submissions (13.9 MB)

# def toLowerCase(self, s: str) -> str:
#     return s.lower()
