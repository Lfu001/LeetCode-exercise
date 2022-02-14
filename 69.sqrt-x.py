#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        inf = 0
        sup = x
        while inf <= sup:
            mid = (inf + sup) // 2
            t = mid * mid
            if t > x:
                sup = mid - 1
            elif t < x:
                inf = mid + 1
            else:
                return mid
        return inf - 1

# @lc code=end

# Solution 1
# ans = 0
# while ans * ans <= x:
#     ans += 1
# return ans - 1
