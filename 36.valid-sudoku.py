#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
# Your runtime beats 72.69 % of python3 submissions
# Your memory usage beats 71.42 % of python3 submissions (13.9 MB)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                row = ("row" + str(i), num)
                column = ("col" + str(j), num)
                box = ("box" + str(i // 3) + str(j // 3), num)
                if num == ".":
                    continue
                elif row in seen or column in seen or box in seen:
                    return False
                else:
                    seen.add(row)
                    seen.add(column)
                    seen.add(box)
        return True

# @lc code=end

# Solution 1
# Your runtime beats 46.22 % of python3 submissions
# Your memory usage beats 71.42 % of python3 submissions (14 MB)

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         checkRows = all(self.checkLine(row) for row in board)
#         if not checkRows:
#             return False

#         checkColumns = all(print(list(column)) or self.checkLine(list(column)) for column in zip(*board))
#         if not checkColumns:
#             return False

#         checkBoxes = self.checkBoxes(board)
#         if not checkBoxes:
#             return False

#         return True

#     def checkLine(self, line: List[str]) -> bool:
#         seen = set()
#         for num in line:
#             if num == ".":
#                 continue
#             elif num not in seen:
#                 seen.add(num)
#             else:
#                 return False
#         return True

#     def checkBoxes(self, board: List[List[str]]) -> bool:
#         for boxRow in range(3):
#             for boxColumn in range(3):
#                 seen = set()
#                 for row in range(3):
#                     for column in range(3):
#                         num = board[3 * boxRow + row][3 * boxColumn + column]
#                         if num == ".":
#                             continue
#                         elif num not in seen:
#                             seen.add(num)
#                         else:
#                             return False
#         return True
