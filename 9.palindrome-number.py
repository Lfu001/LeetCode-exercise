#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        lengthIsEven = 0 if len(num) % 2 == 0 else 1
        num_left = num[:len(num) // 2]
        num_right = num[len(num) // 2 + lengthIsEven:][::-1]
        return num_left == num_right

# @lc code=end
