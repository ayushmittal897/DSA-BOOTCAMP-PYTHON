from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(index, current_comb, current_sum):
            if current_sum == target:
                res.append(current_comb[:])
                return
            if current_sum > target:
                return
                
            for i in range(index, len(candidates)):
                # Skip duplicates at the same recursive level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                    
                current_comb.append(candidates[i])
                backtrack(i + 1, current_comb, current_sum + candidates[i])
                current_comb.pop()
                
        backtrack(0, [], 0)
        return res

"""
Approach:
Backtracking with duplicate handling. First, sort the candidates.
In our recursive loop, we iterate from `index` to the end. 
To prevent duplicate combinations, if `candidates[i] == candidates[i-1]` and it's not the first element in this recursive loop (`i > index`), we skip it.
Since we can't reuse elements, we pass `i + 1` to the next recursive call.
"""
