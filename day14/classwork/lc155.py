class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

"""
Approach:
Use two stacks. One for the actual elements, and another to keep track of the minimums.
When pushing, if the value is smaller than or equal to the current minimum, push it to the min_stack.
When popping, if the value being popped is the current minimum, pop it from the min_stack as well.
"""
