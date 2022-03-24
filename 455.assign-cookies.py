#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
# Solution 1 (Sort)
# Time complexity: O(NlogN, N=max(n,m)), Space complexity: O(n+m)
# Your runtime beats 49.68 % of python3 submissions
# Your memory usage beats 46.52 % of python3 submissions (15.8 MB)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        i = 0
        numOfContentChildren = 0

        for cookie in s:
            if i >= len(g):
                break
            if cookie >= g[i]:
                numOfContentChildren += 1
                i += 1

        return numOfContentChildren

# @lc code=end
