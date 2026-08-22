"""
Approach:
Given `n` is a 32-bit signed integer, the maximum power of 3 that fits is 3^19 = 1162261467.
Since 3 is a prime number, any power of 3 must be a divisor of 1162261467.
We simply check if `n > 0` and `1162261467 % n == 0`.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
