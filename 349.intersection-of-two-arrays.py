#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
# Solution 2 (Avoid using built-in set intersection(&))
# Time complexity: O(n+m), Space complexity: O(n+m)
# Your runtime beats 16.51 % of python3 submissions
# Your memory usage beats 78.99 % of python3 submissions (14.1 MB)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) > len(set2):
            set1, set2 = set2, set1
        return [x for x in set1 if x in set2]

# @lc code=end

# Solution 1 (Using built-in set intersection(&))
# Time complexity: (average, worst) = (O(n+m), O(nm)), Space complexity: O(n+m)
# Your runtime beats 60.47 % of python3 submissions
# Your memory usage beats 47.49 % of python3 submissions (14.2 MB)

# def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     return set(nums1) & set(nums2)
