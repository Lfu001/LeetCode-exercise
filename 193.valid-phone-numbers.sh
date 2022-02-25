#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#

# @lc code=start
# Your runtime beats 53.78 % of bash submissions
# Your memory usage beats 53.39 % of bash submissions (3.1 MB)

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -e "^\(([0-9]\{3\}) \|[0-9]\{3\}-\)[0-9]\{3\}-[0-9]\{4\}$" file.txt

# @lc code=end
