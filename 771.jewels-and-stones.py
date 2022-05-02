#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# Solution 3 (str.count)
# Time complexity: O(len(stones)), Space complexity: O(len(jewels))
# Your runtime beats 10.2 % of python3 submissions
# Your memory usage beats 12.35 % of python3 submissions (13.9 MB)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(stones.count, jewels))


# @lc code=end

# Solution 1 (in set)
# Time complexity: O(len(stones)), Space complexity: O(len(jewels))
# Your runtime beats 42.03 % of python3 submissions
# Your memory usage beats 97.09 % of python3 submissions (13.8 MB)

# def numJewelsInStones(self, jewels: str, stones: str) -> int:
#     jewels = set(jewels)
#     return sum(c in jewels for c in stones)


# Solution 2 (in str)
# Time complexity: O(len(stones)), Space complexity: O(len(jewels))
# Your runtime beats 67.81 % of python3 submissions
# Your memory usage beats 60.9 % of python3 submissions (13.8 MB)
