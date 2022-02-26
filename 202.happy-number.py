#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
# Your runtime beats 71.59 % of python3 submissions
# Your memory usage beats 83.85 % of python3 submissions (13.8 MB)
from functools import lru_cache


class Solution:
    def isHappy(self, n: int) -> bool:
        @lru_cache
        def getNext(num: int):
            ans = 0
            while num > 0:
                num, remainder = divmod(num, 10)
                ans += remainder ** 2
            return ans

        walker = n
        runner = getNext(n)

        while runner != 1 and walker != runner:
            walker = getNext(walker)
            runner = getNext(getNext(runner))

        return runner == 1

# @lc code=end

# Solution 1
# Your runtime beats 65.99 % of python3 submissions
# Your memory usage beats 83.85 % of python3 submissions (13.8 MB)

# def isHappy(self, n: int) -> bool:
#     n_list = [n]
#     while n_list[-1] != 1:
#         ans = 0
#         for i in str(n):
#             ans += int(i) ** 2
#         if ans in n_list:
#             return False
#         n = ans
#         n_list.append(ans)
#     return True


# Solution 2
# Your runtime beats 48.5 % of python3 submissions
# Your memory usage beats 58.83 % of python3 submissions (13.9 MB)

# def isHappy(self, n: int) -> bool:
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         ans = 0
#         for i in str(n):
#             ans += int(i) ** 2
#         n = ans
#     return n == 1
