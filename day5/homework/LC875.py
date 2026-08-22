from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = (left + right) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
                
        return res

"""
Approach:
Binary search on the answer (eating speed k).
The minimum speed is 1, maximum is the max pile size.
We test a speed `k` and calculate total hours required.
If it's <= h, it's valid, and we try to find a smaller valid speed (search left).
Otherwise, the speed is too slow, we search right.
"""
