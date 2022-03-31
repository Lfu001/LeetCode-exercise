#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
# Solution 3 (Convert and compare)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 5.85 % of python3 submissions
# Your memory usage beats 11.83 % of python3 submissions (14 MB)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        if word == word.capitalize():
            return True
        return False

# @lc code=end

# Solution 1 (Built-in functions)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 90.42 % of python3 submissions
# Your memory usage beats 97.3 % of python3 submissions (13.8 MB)

# def detectCapitalUse(self, word: str) -> bool:
#     return word.isupper() or word.islower() or word.istitle()


# Solution 2 (Regex)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 50.19 % of python3 submissions
# Your memory usage beats 61.5 % of python3 submissions (13.8 MB)

# def detectCapitalUse(self, word: str) -> bool:
#     return bool(re.compile("^([A-Z]+|[A-Z]?[a-z]+)$").fullmatch(word))


# Solution 3 (Count number of uppercase)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 46.92 % of python3 submissions
# Your memory usage beats 61.5 % of python3 submissions (13.9 MB)

# def detectCapitalUse(self, word: str) -> bool:
#     upperCharCount = sum(c.isupper() for c in word)
#     return ((upperCharCount == len(word)) or (upperCharCount == 0) or (upperCharCount == 1 and word[0].isupper()))
