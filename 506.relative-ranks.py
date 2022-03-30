#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
from typing import List


# @lc code=start
# Solution 2 (Short expression of Solution 1)
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 63.52 % of python3 submissions
# Your memory usage beats 78.69 % of python3 submissions (15.1 MB)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, (len(score) + 1))))
        return list(map(dict(zip(sorted(score, reverse=True), rank)).get, score))

# @lc code=end

# Solution 1 (Hash table: using sorted())
# Time complexity: O(nlogn), Space complexity: O(n)
# Your runtime beats 82.72 % of python3 submissions
# Your memory usage beats 78.69 % of python3 submissions (15 MB)

# def findRelativeRanks(self, score: List[int]) -> List[str]:
#     answer = []
#     medal = {"1": "Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}
#     rankingBoard = dict()
#
#     for i, s in enumerate(sorted(score, reverse=True)):
#         rankingBoard[s] = str(i + 1)
#
#     for s in score:
#         if (placementNumber := rankingBoard[s]) in {"1", "2", "3"}:
#             answer.append(medal[placementNumber])
#         else:
#             answer.append(rankingBoard[s])
#
#     return answer
