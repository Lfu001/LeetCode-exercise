#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
# Solution 2 (Index list of 1's)
# Time complexity: O(logn), Space complexity: O(logn)
# Your runtime beats 9.53 % of python3 submissions
# Your memory usage beats 56.32 % of python3 submissions (13.8 MB)
class Solution:
    def binaryGap(self, n: int) -> int:
        index = [i for i, val in enumerate(format(n, "b")) if val == "1"]
        return max([b - a for a, b in zip(index, index[1:])] or [0])


# @lc code=end

# Solution 1 (Two pointers)
# Time complexity: O(logn), Space complexity: O(logn)
# Your runtime beats 47.45 % of python3 submissions
# Your memory usage beats 56.32 % of python3 submissions (13.9 MB)

# def binaryGap(self, n: int) -> int:
#     binary = format(n, "b")
#     p1, p2 = 0, 1
#     distance = 0
#     while True:
#         while p2 < len(binary) and binary[p2] != "1":
#             p2 += 1
#         if p2 < len(binary):
#             distance = max((p2 - p1), distance)
#             p1 = p2
#             p2 += 1
#         else:
#             return distance
