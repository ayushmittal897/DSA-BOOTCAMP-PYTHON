class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

"""
Approach:
Dynamic Programming. This is identical to the Fibonacci sequence.
To reach step `n`, you can either come from step `n-1` (1 step) or step `n-2` (2 steps).
Thus, `dp[n] = dp[n-1] + dp[n-2]`. We optimize space by only storing the last two steps.
"""
