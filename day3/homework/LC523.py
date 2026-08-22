from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        total = 0
        
        for i, n in enumerate(nums):
            total += n
            remainder = total % k
            
            if remainder not in remainder_map:
                remainder_map[remainder] = i
            elif i - remainder_map[remainder] > 1:
                return True
                
        return False

"""
Approach:
Use prefix sums and modulo arithmetic. If `prefix_sum[i] % k == prefix_sum[j] % k`, 
it means the subarray sum from `j+1` to `i` is a multiple of `k`.
We store the first index we saw a specific remainder in a hash map.
If we see the same remainder again and the distance is > 1, we found a valid subarray.
"""
