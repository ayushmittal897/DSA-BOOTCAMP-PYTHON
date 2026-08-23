from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    stack.pop()
                    a = 0
            if a:
                stack.append(a)
        return stack

"""
Approach:
Use a stack to simulate asteroid collisions.
A collision only happens if a right-moving asteroid (positive) is on the stack and a left-moving asteroid (negative) comes next.
We resolve collisions by comparing their absolute sizes. If they match, both explode. Otherwise, the smaller one explodes.
"""
