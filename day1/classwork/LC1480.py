from typing import List
"""
Approach:
We need to calculate the running sum of an array.
We can do this by iterating through the array starting from the second element (index 1),
and adding the previous element's value to the current element.
This modifies the array in-place, which saves memory.
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Start from the second element
        for i in range(1, len(nums)):
            # Add the previous sum to the current element
            nums[i] += nums[i - 1]
        return nums
