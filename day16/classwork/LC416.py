from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
            
        target = sum(nums) // 2
        dp = set([0])
        
        for num in nums:
            next_dp = set()
            for t in dp:
                if t + num == target:
                    return True
                next_dp.add(t + num)
                next_dp.add(t)
            dp = next_dp
            
        return target in dp

"""
Approach:
Dynamic Programming (Subset Sum).
We want to find if a subset sums to `total_sum // 2`. If total sum is odd, it's impossible.
We use a Set to keep track of all possible sums we can generate. 
For each number, we add it to all existing sums in the set. If we hit the target, we return True.
"""
