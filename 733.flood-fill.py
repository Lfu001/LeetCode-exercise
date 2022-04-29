#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

from typing import List


# @lc code=start
# Solution 1 (Recursive: DFS)
# Time complexity: O(nm), Space complexity: O(nm)
# Your runtime beats 57.2 % of python3 submissions
# Your memory usage beats 15.9 % of python3 submissions (14.3 MB)
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        prevColor = image[sr][sc]
        imageShape = (len(image), len(image[0]))
        if prevColor == newColor:
            return image

        def dfs(row: int, col: int) -> None:
            if image[row][col] == prevColor:
                image[row][col] = newColor
                if 0 <= (row - 1):
                    dfs((row - 1), col)
                if (row + 1) < imageShape[0]:
                    dfs((row + 1), col)
                if 0 <= (col - 1):
                    dfs(row, (col - 1))
                if (col + 1) < imageShape[1]:
                    dfs(row, (col + 1))

        dfs(sr, sc)
        return image


# @lc code=end
