from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        
        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                res.append(current_perm[:])
                return
                
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicate elements if the previous identical element was NOT used
                # in this recursive level.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                    
                used[i] = True
                current_perm.append(nums[i])
                backtrack(current_perm)
                current_perm.pop()
                used[i] = False
                
        backtrack([])
        return res

"""
Approach:
Backtracking. To handle duplicate permutations, we sort `nums` and use a `used` boolean array.
When iterating, we skip an element if it's already `used`.
To avoid duplicates, if the current element is identical to the previous one AND the previous one is NOT `used` (meaning we just backtracked from it at this same depth), we skip it.
"""
