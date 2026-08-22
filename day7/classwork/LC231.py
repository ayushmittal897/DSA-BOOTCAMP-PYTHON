"""
Approach:
A number is a power of two if it has only one set bit in its binary representation. 
For n > 0, the bitwise trick `n & (n - 1)` clears the lowest set bit. 
If the result is 0, then `n` had exactly one set bit, meaning it's a power of two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
