#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
# Solution 3 (Traverse each row and count the number of boundaries)
# Time complexity: O(nm), Space complexity: O(nm)
# Your runtime beats 6.84 % of python3 submissions
# Your memory usage beats 73.51 % of python3 submissions (14.3 MB)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        grid = grid + list(map(list, zip(*grid)))
        for row in grid:
            row = [0] + row + [0]
            for i in range(len(row) - 1):
                if row[i] != row[i + 1]:
                    perimeter += 1
        return perimeter

# @lc code=end

# Solution 1 (Check surrounding and count perimeter)
# Time complexity: O(nm), Space complexity: O(1)
# Your runtime beats 70.2 % of python3 submissions
# Your memory usage beats 73.51 % of python3 submissions (14.2 MB)

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         perimeter = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]:
#                     perimeter += 4 - self.getNumOfSurroundingCells(grid, i, j)
#         return perimeter
#
#     def getNumOfSurroundingCells(self, grid, i, j):
#         numOfSurroundingCells = 0
#         if i - 1 >= 0 and grid[i - 1][j]:
#             numOfSurroundingCells += 1
#         if j - 1 >= 0 and grid[i][j - 1]:
#             numOfSurroundingCells += 1
#         if i + 1 < len(grid) and grid[i + 1][j]:
#             numOfSurroundingCells += 1
#         if j + 1 < len(grid[0]) and grid[i][j + 1]:
#             numOfSurroundingCells += 1
#         return numOfSurroundingCells


# Solution 2 (Count number of cells and boundaries between cells, and lastly, calculate perimeter)
# Time complexity: O(nm), Space complexity: O(1)
# Your runtime beats 95.35 % of python3 submissions
# Your memory usage beats 73.51 % of python3 submissions (14.3 MB)

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         numOfCells = numOfBoundaries = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]:
#                     numOfCells += 1
#                     if i + 1 < len(grid) and grid[i + 1][j]:
#                         numOfBoundaries += 1
#                     if j + 1 < len(grid[0]) and grid[i][j + 1]:
#                         numOfBoundaries += 1
#         return numOfCells * 4 - numOfBoundaries * 2
