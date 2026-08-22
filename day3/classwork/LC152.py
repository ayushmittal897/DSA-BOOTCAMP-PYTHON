from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
                
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)
            
        return res

"""
Approach:
Keep track of both the maximum and minimum product up to the current element.
We need the minimum because a negative number multiplied by a negative minimum can become the new maximum.
If we encounter 0, the current min and max are reset to 1.
"""
