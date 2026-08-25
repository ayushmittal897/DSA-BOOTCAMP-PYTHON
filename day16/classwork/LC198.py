from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2

"""
Approach:
Dynamic Programming.
At any house, we have two choices: rob it (and add money from `rob1` which was two houses ago) 
or don't rob it (and keep `rob2` which is the max money from the previous house).
We update our variables as we traverse the array to get the maximum possible loot.
"""
