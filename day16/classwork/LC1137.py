class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
            
        t0, t1, t2 = 0, 1, 1
        for _ in range(3, n + 1):
            next_t = t0 + t1 + t2
            t0, t1, t2 = t1, t2, next_t
            
        return t2

"""
Approach:
Dynamic Programming (Space Optimized).
Very similar to Fibonacci, but we keep track of the last three numbers instead of two.
We iteratively sum the three previous numbers to compute the next one.
"""
