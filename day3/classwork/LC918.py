from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = 0
        global_max = nums[0]
        global_min = nums[0]
        total = 0
        
        for n in nums:
            cur_max = max(cur_max + n, n)
            global_max = max(global_max, cur_max)
            
            cur_min = min(cur_min + n, n)
            global_min = min(global_min, cur_min)
            
            total += n
            
        return global_max if global_max < 0 else max(global_max, total - global_min)

"""
Approach:
A circular subarray sum is either the standard maximum subarray sum (using Kadane's),
or it spans across the boundary, which equals the total array sum minus the minimum subarray sum.
Calculate both global_max and global_min.
If global_max < 0, all numbers are negative, return global_max.
Otherwise, return the max of global_max and (total - global_min).
"""
