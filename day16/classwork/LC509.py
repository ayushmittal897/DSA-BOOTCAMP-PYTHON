class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

"""
Approach:
Dynamic Programming (Space Optimized).
Instead of keeping an array for all Fibonacci numbers, we only need the last two values 
to compute the next one. We iteratively update these two variables up to n.
Time complexity is O(n), and space complexity is O(1).
"""
