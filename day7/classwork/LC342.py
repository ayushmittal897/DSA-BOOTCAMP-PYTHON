"""
Approach:
First, check if `n` is a power of two (`n > 0` and `n & (n-1) == 0`).
If it is, we need to ensure the single set bit is at an even index (0-indexed).
The hexadecimal mask `0x55555555` (binary 01010101...) has 1s at all even positions.
Thus, `n & 0x55555555` should equal `n`.
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n
