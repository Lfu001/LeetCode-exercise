#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
# Solution 3 (String concatenation: optimized, short code)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 88.63 % of python3 submissions
# Your memory usage beats 19.23 % of python3 submissions (15.1 MB)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzMapping = {3: "Fizz", 5: "Buzz"}
        return [
            "".join(fizzBuzzMapping[key] for key in fizzBuzzMapping if i % key == 0) or str(i)
            for i in range(1, (n + 1))
        ]

# @lc code=end

# Solution 1 (String concatenation)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 52.91 % of python3 submissions
# Your memory usage beats 19.23 % of python3 submissions (15.2 MB)

# def fizzBuzz(self, n: int) -> List[str]:
#     answer = []
#
#     for i in range(1, (n + 1)):
#         element = ""
#         if i % 3 == 0:
#             element += "Fizz"
#         if i % 5 == 0:
#             element += "Buzz"
#         if not element:
#             element = str(i)
#         answer.append(element)
#
#     return answer


# Solution 2 (String concatenation: optimized)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 44.24 % of python3 submissions
# Your memory usage beats 19.23 % of python3 submissions (15.2 MB)

# def fizzBuzz(self, n: int) -> List[str]:
#     answer = []
#     fizzBuzzMapping = {3: "Fizz", 5: "Buzz"}
#
#     for i in range(1, (n + 1)):
#         element = ""
#         for key in fizzBuzzMapping:
#             if i % key == 0:
#                 element += fizzBuzzMapping[key]
#         if not element:
#             element = str(i)
#         answer.append(element)
#
#     return answer
