"""
Approach:
We can use dynamic programming (bottom-up approach) to save space.
Instead of an array to store all Fibonacci numbers, we only need to track the last two numbers 
to compute the next one, reducing the space complexity to O(1).
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
