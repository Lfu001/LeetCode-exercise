#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
# Solution 3 (Recursive)
# Time complexity: O(log7(n)), Space complexity: O(1)
# Your runtime beats 95.85 % of python3 submissions
# Your memory usage beats 14 % of python3 submissions (14 MB)
class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = "-" if num < 0 else ""

        def positiveBase7(num):
            if not num:
                return ""
            return positiveBase7(num // 7) + str(num % 7)

        return sign + positiveBase7(abs(num)) or "0"

# @lc code=end

# Solution 1 (divmod and reverse at the end)
# Time complexity: O(log7(n)), Space complexity: O(1)
# Your runtime beats 32.98 % of python3 submissions
# Your memory usage beats 14 % of python3 submissions (13.9 MB)

# def convertToBase7(self, num: int) -> str:
#     sign = ""
#     if num < 0:
#         num = -num
#         sign = "-"
#
#     base7Repr = ""
#
#     while True:
#         num, r = divmod(num, 7)
#         base7Repr += str(r)
#         if not num:
#             break
#
#     return (base7Repr + sign)[::-1]


# Solution 2 (Simplify solution 1)
# Time complexity: O(log7(n)), Space complexity: O(1)
# Your runtime beats 57.3 % of python3 submissions
# Your memory usage beats 64.77 % of python3 submissions (13.9 MB)


sol = Solution()
print(sol.convertToBase7(-1))
