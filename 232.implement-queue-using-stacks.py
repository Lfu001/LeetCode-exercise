#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
# Your runtime beats 84.99 % of python3 submissions
# Your memory usage beats 99.35 % of python3 submissions (13.9 MB)
class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

# Solution 1
# Your runtime beats 56.77 % of python3 submissions
# Your memory usage beats 88.4 % of python3 submissions (14 MB)

# class MyQueue:

#     def __init__(self):
#         self.stack = list()

#     def push(self, x: int) -> None:
#         stack_tmp = []
#         while self.stack:
#             stack_tmp.append(self.stack.pop())
#         self.stack.append(x)
#         while stack_tmp:
#             self.stack.append(stack_tmp.pop())

#     def pop(self) -> int:
#         return self.stack.pop()

#     def peek(self) -> int:
#         return self.stack[-1]

#     def empty(self) -> bool:
#         return not self.stack


# Solution 2
# Your runtime beats 84.99 % of python3 submissions
# Your memory usage beats 56.72 % of python3 submissions (14.1 MB)

# def peek(self) -> int:
#     if not self.stack2:
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#     return self.stack2[-1]
