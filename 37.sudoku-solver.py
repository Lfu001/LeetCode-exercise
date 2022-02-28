#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
# Your runtime beats 29.38 % of python3 submissions
# Your memory usage beats 72.55 % of python3 submissions (14.1 MB)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        emptyCells = self.getEmptyCells(board)
        self.backtrack(board, emptyCells)

    def backtrack(self, board: List[List[str]], emptyCells, currentCell=0) -> bool:
        if currentCell >= len(emptyCells):
            return True
        i, j = emptyCells[currentCell]
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.checkAroundMe(board, i, j, num):
                board[i][j] = num
                if self.backtrack(board, emptyCells, currentCell + 1):
                    return True
                board[i][j] = "."
        return False

    def checkAroundMe(self, board: List[List[str]], rowIndex: int, columnIndex: int, num: int) -> bool:
        def cellAroundMeGenerator():
            yield board[rowIndex]
            yield list(zip(*board))[columnIndex]
            myBoxRow = rowIndex // 3 * 3
            myBoxColumn = columnIndex // 3 * 3
            yield (board[myBoxRow + row][myBoxColumn + col] for row in range(3) for col in range(3))
        for line in cellAroundMeGenerator():
            if num in line:
                return False
        return True

    def getEmptyCells(self, board: List[List[str]]) -> List[tuple[int, int]]:
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    emptyCells.append((i, j))
        return emptyCells

# @lc code=end
