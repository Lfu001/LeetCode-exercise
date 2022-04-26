#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
# Solution 1
# Time complexity: {__init__: O(1), put,get,remove: O(k) (k=number of collision)}
# Space complexity: O(1)
# Your runtime beats 88.85 % of python3 submissions
# Your memory usage beats 83.51 % of python3 submissions (17.1 MB)
class MyHashMap:
    def __init__(self):
        self.keys = [[] for _ in range(1 << 10)]
        self.values = [[] for _ in range(1 << 10)]

    def put(self, key: int, value: int) -> None:
        digest = self._hash(key)
        if key in self.keys[digest]:
            self.values[digest][self.keys[digest].index(key)] = value
        else:
            self.keys[digest].append(key)
            self.values[digest].append(value)

    def get(self, key: int) -> int:
        digest = self._hash(key)
        if key in self.keys[digest]:
            return self.values[digest][self.keys[digest].index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        digest = self._hash(key)
        if key in self.keys[digest]:
            idx = self.keys[digest].index(key)
            del self.keys[digest][idx]
            del self.values[digest][idx]

    def _hash(self, key) -> int:
        return ((13177579 * key) & ((1 << 20) - 1)) >> 10


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
