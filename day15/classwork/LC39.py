from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(index, current_comb, current_sum):
            if current_sum == target:
                res.append(current_comb[:])
                return
            if current_sum > target or index >= len(candidates):
                return
                
            # Choice 1: Include current candidate (and we can reuse it, so index stays the same)
            current_comb.append(candidates[index])
            backtrack(index, current_comb, current_sum + candidates[index])
            current_comb.pop()
            
            # Choice 2: Skip current candidate and move to the next
            backtrack(index + 1, current_comb, current_sum)
            
        backtrack(0, [], 0)
        return res

"""
Approach:
Backtracking. We can reuse elements, so at each step we make a choice:
1. Include the current candidate, add it to our sum, and stay on the same index (to possibly use it again).
2. Skip the current candidate and move to the next index.
We stop if our sum exceeds the target. If it equals the target, we found a valid combination.
"""
