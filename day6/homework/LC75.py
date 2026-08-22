from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

"""
Approach:
Dutch National Flag algorithm.
Use three pointers: `low` for 0s, `mid` for traversing, and `high` for 2s.
Iterate `mid` until it passes `high`.
If we see a 0, swap it with the element at `low`, increment both `low` and `mid`.
If we see a 1, just increment `mid`.
If we see a 2, swap it with the element at `high` and decrement `high` (don't increment `mid` yet, as the swapped element needs to be checked).
"""
