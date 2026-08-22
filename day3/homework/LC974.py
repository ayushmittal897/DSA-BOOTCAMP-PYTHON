from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = {0: 1}
        res = 0
        cur_sum = 0
        
        for n in nums:
            cur_sum += n
            remainder = cur_sum % k
            if remainder < 0:
                remainder += k
                
            res += remainder_map.get(remainder, 0)
            remainder_map[remainder] = remainder_map.get(remainder, 0) + 1
            
        return res

"""
Approach:
Similar to checking subarray sums. 
If the prefix sums at two indices have the same remainder when divided by `k`, 
the subarray between them has a sum divisible by `k`.
We keep a frequency map of remainders and add the frequency to our result when we see it again.
"""
