#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
# Solution 1 (Enumerate cases)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 8.29 % of python3 submissions
# Your memory usage beats 62.71 % of python3 submissions (14.2 MB)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        buddy = []
        for a, b in zip(s, goal):
            if a != b:
                if len(buddy) > 1:
                    return False
                buddy.append((a, b))
        return len(buddy) == 2 and buddy[0] == buddy[1][::-1]


# @lc code=end
