#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
# Solution 2 (Two pointers)
# Time complexity: O(n), Space complexity: O(1)
# Your runtime beats 38.45 % of python3 submissions
# Your memory usage beats 34.32 % of python3 submissions (13.9 MB)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)


# @lc code=end

# Solution 1 (itertools.groupby)
# Time complexity: O(min(m,n)), Space complexity: O(m+n)
# Your runtime beats 38.45 % of python3 submissions
# Your memory usage beats 34.32 % of python3 submissions (13.9 MB)

# def isLongPressedName(self, name: str, typed: str) -> bool:
#     return not any(
#         (not name_group)
#         or (not typed_group)
#         or name_group[0] != typed_group[0]
#         or len(list(name_group[1])) > len(list(typed_group[1]))
#         for name_group, typed_group in zip_longest(groupby(name), groupby(typed))
#     )
