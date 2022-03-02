#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
# # Your runtime beats 37.36 % of python3 submissions
# Your memory usage beats 60.73 % of python3 submissions (14 MB)
from collections import deque


class MyStack:

    def __init__(self):
        self.reversedQueue = deque()

    def push(self, x: int) -> None:
        sizeOfReversedQueue = len(self.reversedQueue)
        self.reversedQueue.append(x)
        for _ in range(sizeOfReversedQueue):
            self.reversedQueue.append(self.reversedQueue.popleft())

    def pop(self) -> int:
        return self.reversedQueue.popleft()

    def top(self) -> int:
        return self.reversedQueue[0]

    def empty(self) -> bool:
        return len(self.reversedQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
