#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        for i in range((m + n + 1), -1, -1):
            if n < 0:
                break
            if m < 0:
                nums1[:(i + 1)] = nums2[:(n + 1)]
                break

            if nums1[m] <= nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1

# @lc code=end

# Solution 1
# nums1[m:] = nums2
# nums1.sort()
