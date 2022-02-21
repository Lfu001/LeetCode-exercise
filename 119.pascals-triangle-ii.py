#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row.append(0)
            for i in range((len(row) - 1), 0, -1):
                row[i] += row[i - 1]
        return row

# @lc code=end

# Solution 1
# row = [1]
# for _ in range(rowIndex):
#     row = [sum(i) for i in zip((row + [0]), ([0] + row))]
# return row
