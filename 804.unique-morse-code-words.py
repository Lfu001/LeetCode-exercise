#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

from typing import List


# @lc code=start
# Solution 1 (Set)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 5.27 % of python3 submissions
# Your memory usage beats 75.02 % of python3 submissions (13.8 MB)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        transformation = set()

        for word in words:
            transformation.add("".join(code[ord(c) - ord("a")] for c in word))

        return len(transformation)


# @lc code=end
