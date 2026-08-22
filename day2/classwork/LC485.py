from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        
        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
                
        return max_ones

"""
Approach:
We iterate through the array. 
If we encounter a 1, we increment our current count and update the maximum count.
If we encounter a 0, we reset our current count to 0.
This takes O(N) time and O(1) space.
"""
