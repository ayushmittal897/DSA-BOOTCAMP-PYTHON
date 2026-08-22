from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res

"""
Approach:
Boyer-Moore Voting Algorithm.
Since the majority element appears more than n/2 times, its count will outlast all other elements combined.
Maintain a candidate `res` and a `count`. Increment if the current element matches `res`, decrement otherwise.
If `count` drops to 0, pick a new candidate.
"""
