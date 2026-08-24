from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(index, current_subset):
            res.append(current_subset[:])
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return res

"""
Approach:
Backtracking. Very similar to Subsets I, but to handle duplicates, we must sort the array first.
Inside our loop, if we encounter an element that is the same as the previous element (and it's not the first iteration of the loop `i > index`), we skip it.
This ensures we don't generate duplicate subsets.
"""
