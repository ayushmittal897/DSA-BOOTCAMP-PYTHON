from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, current_comb):
            if len(current_comb) == k:
                res.append(current_comb[:])
                return
                
            for i in range(start, n + 1):
                current_comb.append(i)
                backtrack(i + 1, current_comb)
                current_comb.pop()
                
        backtrack(1, [])
        return res

"""
Approach:
Backtracking. We want to find all combinations of `k` numbers from `1` to `n`.
We start from 1. If our `current_comb` length reaches `k`, we add it to results and return.
Otherwise, we loop from `start` to `n`, append `i`, recurse with `i + 1`, and then backtrack (pop).
"""
