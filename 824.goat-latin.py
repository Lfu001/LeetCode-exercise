#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
# Solution 3 (Generator version of Solution 2)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 75.42 % of python3 submissions
# Your memory usage beats 63.95 % of python3 submissions (13.9 MB)
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def goatLatinGenerator(s: str):
            vowel = set("aeiouAEIOU")
            for i, word in enumerate(s.split()):
                if not word[0] in vowel:
                    word = word[1:] + word[0]
                yield (word + "ma" + "a" * (i + 1))

        return " ".join(goatLatinGenerator(sentence))


# @lc code=end

# Solution 1 (Process each word and join)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 49.56 % of python3 submissions
# Your memory usage beats 63.95 % of python3 submissions (13.9 MB)

# def toGoatLatin(self, sentence: str) -> str:
#     ans = []
#     for i, word in enumerate(sentence.split()):
#         if word[0].lower() in {"a", "e", "i", "o", "u"}:
#             newWord = word
#         else:
#             newWord = word[1:] + word[0]
#         newWord += "ma" + "a" * (i + 1)
#         ans.append(newWord)
#     return " ".join(ans)


# Solution 2 (Simplified version of Solution 1)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 9.86 % of python3 submissions
# Your memory usage beats 63.95 % of python3 submissions (13.8 MB)

# def toGoatLatin(self, sentence: str) -> str:
#     ans = []
#     vowel = set("aeiouAEIOU")
#     for i, word in enumerate(sentence.split()):
#         if not word[0] in vowel:
#             word = word[1:] + word[0]
#         ans.append(word + "ma" + "a" * (i + 1))
#     return " ".join(ans)
