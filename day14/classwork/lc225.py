from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate the queue to make the newly added element the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

"""
Approach:
Implement a Stack using a single Queue (deque).
When pushing an element, we add it to the back of the queue, 
and then immediately pop from the front and push to the back `size-1` times.
This effectively reverses the order, making the queue behave like a stack.
"""
