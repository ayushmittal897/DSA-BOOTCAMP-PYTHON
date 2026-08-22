from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sums = {0: 1}
        
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            
            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            
        return res

"""
Approach:
Use a prefix sum and a hash map. `prefix_sums` stores the frequency of each prefix sum seen so far.
For each element, we calculate the current prefix sum. We want a previous prefix sum that equals `cur_sum - k`.
If it exists in the hash map, we add its frequency to our result.
"""
