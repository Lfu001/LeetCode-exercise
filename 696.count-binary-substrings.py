#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
# Solution 2 (Optimezed version of solution 1)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 58.75 % of python3 submissions
# Your memory usage beats 44.01 % of python3 submissions (14.6 MB)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        return ans + min(prev, curr)

# @lc code=end

# Solution 1 (Grouping: itertools.groupby)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 91.19 % of python3 submissions
# Your memory usage beats 44.01 % of python3 submissions (14.6 MB)

# def countBinarySubstrings(self, s: str) -> int:
#     numOfElementInEachGroup = [len(list(group)) for _, group in groupby(s)]
#     return sum(min(x, y) for x, y in zip(numOfElementInEachGroup, numOfElementInEachGroup[1:]))
