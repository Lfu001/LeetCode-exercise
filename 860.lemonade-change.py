#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

from typing import List


# @lc code=start
# Solution 2 (Simulation)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 91.58 % of python3 submissions
# Your memory usage beats 88.5 % of python3 submissions (17.7 MB)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                if five:
                    five -= 1
                else:
                    return False
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# @lc code=end

# Solution 1 (Simulation: collections.Counter)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 46.54 % of python3 submissions
# Your memory usage beats 52.99 % of python3 submissions (18 MB)

# def lemonadeChange(self, bills: List[int]) -> bool:
#     billCounter = Counter()
#     for b in bills:
#         billCounter[b] += 1
#         if b == 10:
#             if billCounter.get(5, 0):
#                 billCounter[5] -= 1
#             else:
#                 return False
#         elif b == 20:
#             if billCounter.get(5, 0) and billCounter.get(10, 0):
#                 billCounter[5] -= 1
#                 billCounter[10] -= 1
#             elif billCounter.get(5, 0) >= 3:
#                 billCounter[5] -= 3
#             else:
#                 return False
#     return True
