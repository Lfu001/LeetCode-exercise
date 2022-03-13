#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# Solution 3 (Bit manipulation) Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 99.96 % of python3 submissions
# Your memory usage beats 37.66 % of python3 submissions (20.8 MB)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans

# @lc code=end

# Solution 1 (Count bits) Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 61.89 % of python3 submissions
# Your memory usage beats 37.66 % of python3 submissions (20.9 MB)

# def countBits(self, n: int) -> List[int]:
#     ans = []
#     for i in range(n + 1):
#         ans.append(format(i, "b").count("1"))
#     return ans


# Solution 2 (Generator) Time complexcity: O(n), Space complexity: O(n)
# Your runtime beats 78.03 % of python3 submissions
# Your memory usage beats 83.2 % of python3 submissions (20.7 MB)

# def countBits(self, n: int) -> List[int]:
#     ans = [0]
#     if n > 0:
#         for i in range(1, n + 1):
#             if 65536 % i == 0:
#                 numOfOneGenerator = ((numOfOne + 1) for numOfOne in ans)
#             ans.append(next(numOfOneGenerator))
#     return ans
