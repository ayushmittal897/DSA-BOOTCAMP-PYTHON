from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
        return count <= 1

"""
Approach:
In a sorted and rotated array, there can be at most one place where an element is strictly greater than the next element.
We can check this condition for all adjacent pairs (including the last and first elements).
If the count of such breaks is > 1, it's not a sorted and rotated array.
"""
