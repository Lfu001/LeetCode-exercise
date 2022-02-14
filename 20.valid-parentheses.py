#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        parentheses = {"open": ["(", "{", "["], "closed": [")", "}", "]"]}
        stack_ = list()

        for c in s:
            if c in parentheses["open"]:
                stack_.append(c)
            else:
                if len(stack_) == 0:
                    return False
                if parentheses["closed"].index(c) != parentheses["open"].index(stack_.pop()):
                    return False

        if len(stack_) != 0:
            return False

        return True

# @lc code=end
