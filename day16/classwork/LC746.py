from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])

"""
Approach:
Dynamic Programming (Bottom-Up).
We modify the `cost` array in-place, adding a `0` at the end to represent the top of the stairs.
Starting from the third to last step, we add the minimum cost of taking 1 step or 2 steps from there.
We do this backwards to the start. The answer is the minimum of starting at index 0 or index 1.
"""
