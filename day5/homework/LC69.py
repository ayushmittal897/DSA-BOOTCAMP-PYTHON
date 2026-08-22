class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                res = mid
                left = mid + 1
            else:
                return mid
                
        return res

"""
Approach:
Binary search for the integer square root.
The answer lies in the range [0, x].
We guess `mid` and square it. If it's too large, we search the left half.
If it's too small, we update our best result and search the right half.
"""
