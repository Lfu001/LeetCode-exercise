#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
# Solution 3 (Hash table)
# Time complexity: O(n+m), Space complexity: O(min(n,m))
# Your runtime beats 45.64 % of python3 submissions
# Your memory usage beats 67.46 % of python3 submissions (14 MB)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = dict()
        result = list()

        for num in nums1:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result

# @lc code=end

# Solution 1 (Hash table)
# Time complexity: O(nm), Space complexity: O(min(n,m))
# Your runtime beats 9.66 % of python3 submissions
# Your memory usage beats 91.67 % of python3 submissions (14 MB)

# def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#
#     count = dict()
#
#     for num in nums1:
#         if num not in count:
#             count[num] = 0
#         count[num] += 1
#
#     ans = list()
#
#     for key in count:
#         ans += [key] * min(nums2.count(key), count[key])
#
#     return ans


# Solution 2 (Two pointers: sort)
# Time complexity: O(nlogn+mlogm), Space complexity: O(n+m)
# Your runtime beats 30.15 % of python3 submissions
# Your memory usage beats 91.67 % of python3 submissions (14 MB)

# def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     nums1 = sorted(nums1)
#     nums2 = sorted(nums2)
#
#     result = list()
#     p1, p2 = 0, 0
#
#     while p1 < len(nums1) and p2 < len(nums2):
#         if nums1[p1] < nums2[p2]:
#             p1 += 1
#         elif nums1[p1] > nums2[p2]:
#             p2 += 1
#         else:
#             result.append(nums1[p1])
#             p1 += 1
#             p2 += 1
#
#     return result
