"""
Approach:
String S_n has length L = 2^n - 1. Its middle bit is always '1' (at k = L // 2 + 1).
The first half is identical to S_{n-1}. 
The second half is the reverse-complement of S_{n-1}.
We recursively find the bit based on whether `k` falls in the left half, is the middle bit, or the right half.
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
            
        length = (1 << n) - 1
        mid = length // 2 + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # Find the corresponding mirrored bit in the first half and invert it
            mirrored_k = length - k + 1
            res = self.findKthBit(n - 1, mirrored_k)
            return "0" if res == "1" else "1"
