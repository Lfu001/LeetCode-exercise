#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

import bisect
from collections import deque
from typing import List


# @lc code=start
# Solution 2 (Store top k elements)
# Time complexity: __init__: O(nlogn), add: O(logk)
# Space complexity: (k)
# Your runtime beats 46.47 % of python3 submissions
# Your memory usage beats 12.98 % of python3 submissions (18.4 MB)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.topK = deque(sorted(nums)[-k:])

    def add(self, val: int) -> int:
        self.nums.append(val)
        bisect.insort_left(self.topK, val)
        if len(self.topK) > self.k:
            self.topK.popleft()
        return self.topK[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

# Solution 1 (Sort)
# Time complexity: __init__: O(1), add: O(nlogn)
# Space complexity: (1)
# Your runtime beats 13.02 % of python3 submissions
# Your memory usage beats 34.49 % of python3 submissions (18.4 MB)

# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums
#
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort()
#         return self.nums[-self.k]
