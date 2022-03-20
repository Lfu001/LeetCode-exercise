#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
# Solution 2 (Brute force: Loop in loop)
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 31.57 % of python3 submissions
# Your memory usage beats 98.35 % of python3 submissions (13.8 MB)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []

        possibleTimes = list()

        for hour in range(12):
            for minute in range(60):
                if sum(bin(i).count("1") for i in (hour, minute)) == turnedOn:
                    possibleTimes.append("{}:{:02}".format(hour, minute))

        return possibleTimes

# @lc code=end

# Solution 1 (Brute force: itertools.product())
# Time complexity: O(1), Space complexity: O(1)
# Your runtime beats 55.54 % of python3 submissions
# Your memory usage beats 98.35 % of python3 submissions (13.8 MB)

# def readBinaryWatch(self, turnedOn: int) -> List[str]:
#     if turnedOn >= 9:
#         return []
#
#     possibleTimes = list()
#
#     for time in product(range(12), range(60)):
#         if sum(bin(i).count("1") for i in time) == turnedOn:
#             possibleTimes.append("{}:{:02}".format(*time))
#
#     return possibleTimes
