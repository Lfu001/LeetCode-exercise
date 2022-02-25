#
# @lc app=leetcode id=195 lang=bash
#
# [195] Tenth Line
#

# @lc code=start
# Your runtime beats 25.92 % of bash submissions
# Your memory usage beats 78.95 % of bash submissions (3.6 MB)

# Read from the file file.txt and output the tenth line to stdout.
head -n 10 file.txt | tail -n +10

# @lc code=end
