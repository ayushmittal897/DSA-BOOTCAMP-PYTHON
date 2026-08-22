"""
Approach:
We use fast exponentiation (exponentiation by squaring) which works in O(log n) time.
If `n` is negative, we can compute `(1/x)^(-n)`.
At each step, if `n` is even, `x^n = (x^2)^(n/2)`.
If `n` is odd, `x^n = x * x^(n-1)`.
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0
        curr_prod = x
        while n > 0:
            if n % 2 == 1:
                res *= curr_prod
            curr_prod *= curr_prod
            n //= 2
        return res
