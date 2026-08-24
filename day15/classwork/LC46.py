from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                res.append(current_perm[:])
                return
                
            for num in nums:
                if num not in current_perm:
                    current_perm.append(num)
                    backtrack(current_perm)
                    current_perm.pop()
                    
        backtrack([])
        return res

"""
Approach:
Backtracking. We want to build permutations, so order matters and we use all elements.
In our recursive function, we loop through all numbers in `nums`.
If a number is already in our `current_perm`, we skip it (since all numbers are distinct).
Otherwise, we add it, recurse, and then backtrack.
"""
