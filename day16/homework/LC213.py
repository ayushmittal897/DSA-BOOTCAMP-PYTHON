from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        return max(helper(nums[:-1]), helper(nums[1:]))

"""
Approach:
Dynamic Programming.
Since the houses are circular, the first and last houses are connected. 
We cannot rob both. Thus, the problem reduces to finding the max of two scenarios:
1. Robbing from house 0 to n-2 (excluding the last).
2. Robbing from house 1 to n-1 (excluding the first).
We use the standard House Robber logic for both and take the maximum.
"""
