#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
# Solution 3 (Convert to ASCII code: without itertools.zip_longest)
# Time complexity: O(max(n,m)), Space complexity O(1)
# Your runtime beats 64.16 % of python3 submissions
# Your memory usage beats 74.99 % of python3 submissions (13.9 MB)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        for _ in range(max(len(num1), len(num2))):
            n1 = n2 = 0
            if i >= 0:
                n1 = ord(num1[i]) - ord("0")
            if j >= 0:
                n2 = ord(num2[j]) - ord("0")
            digitSum = n1 + n2 + carry
            carry = digitSum // 10
            ans += str(digitSum % 10)
            i -= 1
            j -= 1

        if carry:
            ans += str(carry)

        return ans[::-1]

# @lc code=end

# Solution 1 (Convert to int)
# Time complexity: O(max(n,m)), Space complexity O(1)
# Your runtime beats 5.04 % of python3 submissions
# Your memory usage beats 94.27 % of python3 submissions (13.9 MB)

# def addStrings(self, num1: str, num2: str) -> str:
#     ans = 0
#     for i, (n1, n2) in enumerate(zip_longest(reversed(num1), reversed(num2), fillvalue=0)):
#         ans += 10 ** i * (int(n1) + int(n2))
#     return str(ans)


# Solution 2 (Convert to ASCII code)
# Time complexity: O(max(n,m)), Space complexity O(1)
# Your runtime beats 5.04 % of python3 submissions
# Your memory usage beats 94.27 % of python3 submissions (13.9 MB)

# def addStrings(self, num1: str, num2: str) -> str:
#     ans = 0
#     for i, ns in enumerate(zip_longest(reversed(num1), reversed(num2), fillvalue="0")):
#         ans += 10 ** i * sum(ord(n) - ord("0") for n in ns)
#     return str(ans)
