from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, current_subset):
            res.append(current_subset[:])
            
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return res

"""
Approach:
Backtracking. To generate all subsets, at each step we can either include the current element or skip it.
We append the `current_subset` to our result at the beginning of the backtrack function (capturing all lengths).
Then we loop through the remaining elements, add an element, recursively call backtrack for the next index, and then pop the element to explore other choices.
"""
