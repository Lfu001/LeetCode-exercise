#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
# Solution 2 (Maximum number of hash collision: approximately 20)
# Time complexity: {add: O(1), remove: O(1), contains: O(1), hash: O(1)}
# Space complexity: O(1)
# Your runtime beats 81.37 % of python3 submissions
# Your memory usage beats 48.27 % of python3 submissions (19.3 MB)
class MyHashSet:
    def __init__(self):
        self.mapping = [[] for _ in range(1 << 10)]

    def add(self, key: int) -> None:
        digest = self._hash(key)
        if key not in self.mapping[digest]:
            self.mapping[digest].append(key)

    def remove(self, key: int) -> None:
        digest = self._hash(key)
        if key in self.mapping[digest]:
            self.mapping[digest].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.mapping[self._hash(key)]

    def _hash(self, key) -> int:
        return ((13177579 * key) & ((1 << 20) - 1)) >> 10


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

# Solution 1 (Maximum number of hash collision: approximately 5)
# Time complexity: {add: O(1), remove: O(1), contains: O(1), hash: O(1)}
# Space complexity: O(1)
# Your runtime beats 27.84 % of python3 submissions
# Your memory usage beats 19.92 % of python3 submissions (22.2 MB)

# class MyHashSet:
#     def __init__(self):
#         self.mapping = [[] for _ in range(1 << 15)]
#
#     def add(self, key: int) -> None:
#         digest = self._hash(key)
#         if key not in self.mapping[digest]:
#             self.mapping[digest].append(key)
#
#     def remove(self, key: int) -> None:
#         digest = self._hash(key)
#         if key in self.mapping[digest]:
#             self.mapping[digest].remove(key)
#
#     def contains(self, key: int) -> bool:
#         return key in self.mapping[self._hash(key)]
#
#     def _hash(self, key) -> int:
#         return ((13177579 * key) & ((1 << 20) - 1)) >> 5
