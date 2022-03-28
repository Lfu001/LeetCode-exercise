#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List


# @lc code=start
# Solution 2 (Monotonic stack)
# Time complexity: O(n+m), Space complexity: O(m)
# Your runtime beats 75.55 % of python3 submissions
# Your memory usage beats 60.9 % of python3 submissions (14.1 MB)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ansMap = dict()
        decStack = list()
        for n in nums2:
            while decStack and decStack[-1] < n:
                ansMap[decStack.pop()] = n
            decStack.append(n)
        return [ansMap.get(n, -1) for n in nums1]

# @lc code=end

# Solution 1 (Brute force)
# Time complexity: O(nm), Space complexity: O(1)
# Your runtime beats 52.74 % of python3 submissions
# Your memory usage beats 96.16 % of python3 submissions (14 MB)

# def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     ans = []
#     for n in nums1:
#         nextGreaterElement = -1
#         indexOfNInNums2 = nums2.index(n)
#         for i in range(indexOfNInNums2 + 1, len(nums2)):
#             if nums2[i] > nums2[indexOfNInNums2]:
#                 nextGreaterElement = nums2[i]
#                 break
#         ans.append(nextGreaterElement)
#     return ans
