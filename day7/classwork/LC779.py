"""
Approach:
The grammar tree builds recursively where row `n`'s first half is exactly row `n-1` 
and the second half is the complement of row `n-1`.
If `k` is in the first half (k <= mid), the bit is the same as `k` in row `n-1`.
If `k` is in the second half, the bit is the complement of `k - mid` in row `n-1`.
"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        mid = 2 ** (n - 2)
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)
