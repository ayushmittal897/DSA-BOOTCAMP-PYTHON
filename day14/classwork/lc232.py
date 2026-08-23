class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

"""
Approach:
Use two stacks. `s1` is used for pushing elements.
When we need to pop or peek, we check if `s2` is empty. If it is, we pour all elements from `s1` into `s2`.
This reverses their order, so the bottom of `s1` (the oldest element) becomes the top of `s2`, matching queue behavior.
"""
