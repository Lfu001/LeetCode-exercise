#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
from typing import List


# @lc code=start
# Solution 3 (Sum up the smaller of duration or time interval from the attack to the next attack)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 52.47 % of python3 submissions
# Your memory usage beats 50.77 % of python3 submissions (15.6 MB)
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalPoisonedSeconds = 0

        if not duration:
            return totalPoisonedSeconds

        for i in range(len(timeSeries) - 1):
            totalPoisonedSeconds += min(duration, (timeSeries[i + 1] - timeSeries[i]))

        return totalPoisonedSeconds + duration

# @lc code=end

# × Time Limit Exceeded
# Solution 1 (Set)
# Time complexity: O(nm), Space complexity: O(nm)

# def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#     poisonedSeconds = set()
#     for t in timeSeries:
#         for i in range(duration):
#             poisonedSeconds.add(t + i)
#     return len(poisonedSeconds)


# Solution 2 (Merge intervals by bisect.bisect_right)
# Time complexity: O(nlogm), Space complexity: O(1)
# Your runtime beats 16.67 % of python3 submissions
# Your memory usage beats 92.94 % of python3 submissions (15.4 MB)

# def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#     poisonedSeconds = 0

#     if not duration:
#         return poisonedSeconds

#     i = resetTimeIndex = 0

#     while i < len(timeSeries):
#         x = bisect_right(timeSeries, (timeSeries[resetTimeIndex] + duration - 1))
#         if (x - 1) == resetTimeIndex:
#             poisonedSeconds += timeSeries[resetTimeIndex] + duration - timeSeries[i]
#             i = resetTimeIndex = x
#         else:
#             resetTimeIndex = x - 1

#     return poisonedSeconds
