#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows - 1):
            row = [sum(i) for i in zip((ans[-1] + [0]), ([0] + ans[-1]))]
            ans.append(row)
        return ans

# @lc code=end

# Solution 1
# ans = [[1]]
# for i in range(1, numRows):
#     row = [0] * (i + 1)
#     for j, n in enumerate(ans[-1]):
#         row[j] += n
#         row[j + 1] += n
#     ans.append(row)
# return ans
