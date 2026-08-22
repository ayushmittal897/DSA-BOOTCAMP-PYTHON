"""
Approach:
Climbing stairs is equivalent to the Fibonacci sequence. To reach step `i`, 
one must step from either `i-1` or `i-2`. Thus, `ways(i) = ways(i-1) + ways(i-2)`.
We can track the last two steps to achieve O(n) time and O(1) space.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
