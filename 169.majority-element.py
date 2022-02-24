#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# Time complexity: O(n)
# Your runtime beats 12.54 % of python3 submissions
# Your memory usage beats 79.56 % of python3 submissions (15.5 MB)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = None

        for n in nums:
            if count == 0:
                ans = n
            count += 1 if n == ans else -1

        return ans

# @lc code=end

# Solution 1   Time complexity: O(nlogn)
# Your runtime beats 30.75 % of python3 submissions
# Your memory usage beats 79.56 % of python3 submissions (15.5 MB)

# def majorityElement(self, nums: List[int]) -> int:
#     return Counter(nums).most_common(1)[0][0]


# Solution 2   Time complexity: O(n)
# Your runtime beats 18.96 % of python3 submissions
# Your memory usage beats 79.56 % of python3 submissions (15.4 MB)

# def majorityElement(self, nums: List[int]) -> int:
#     counter = Counter(nums)
#     return max(counter.keys(), key=counter.get)
