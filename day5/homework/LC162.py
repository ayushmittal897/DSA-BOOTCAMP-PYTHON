from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if left neighbor is greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # Check if right neighbor is greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            # mid is greater than both neighbors
            else:
                return mid

"""
Approach:
Binary search. A peak element is strictly greater than its neighbors.
We check the middle element. If its left neighbor is greater, a peak must exist in the left half.
If its right neighbor is greater, a peak must exist in the right half.
Otherwise, the middle element itself is a peak.
"""
