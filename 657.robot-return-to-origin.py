#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

from collections import Counter


# @lc code=start
# Solution 4 (built-in: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 89.05 % of python3 submissions
# Your memory usage beats 91.68 % of python3 submissions (14.1 MB)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movesCounter = Counter(moves)
        return movesCounter.get("L", 0) == movesCounter.get("R", 0) and movesCounter.get("U", 0) == movesCounter.get("D", 0)

# @lc code=end

# Solution 1 (Simulation)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 77.89 % of python3 submissions
# Your memory usage beats 41.06 % of python3 submissions (14.1 MB)

# def judgeCircle(self, moves: str) -> bool:
#     x = y = 0
#     for m in moves:
#         if m == "L":
#             x += 1
#         elif m == "R":
#             x -= 1
#         elif m == "U":
#             y += 1
#         else:
#             y -= 1
#     return x == y == 0


# Solution 2 (Complex)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 22.93 % of python3 submissions
# Your memory usage beats 41.06 % of python3 submissions (14.1 MB)

# def judgeCircle(self, moves: str) -> bool:
#     return not sum(1j ** "RUL".find(m) for m in moves)


# Solution 3 (Built-in function: str.count)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 97.37 % of python3 submissions
# Your memory usage beats 5.58 % of python3 submissions (14.2 MB)

# def judgeCircle(self, moves: str) -> bool:
#     return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
