#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

from typing import List


# @lc code=start
# Solution 1 (set)
# Time complexity: O(n), Space complexity: O(n)
# Your runtime beats 80.16 % of python3 submissions
# Your memory usage beats 73.92 % of python3 submissions (13.9 MB)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()
        for address in emails:
            local, domain = address.split("@")
            plus_index = i if (i := local.find("+")) != -1 else None
            valid_emails.add(local[:plus_index].replace(".", "") + "@" + domain)
        return len(valid_emails)


# @lc code=end
