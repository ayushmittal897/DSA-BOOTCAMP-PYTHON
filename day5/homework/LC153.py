from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
                
            mid = (left + right) // 2
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                
        return res

"""
Approach:
Binary search on rotated sorted array.
If the subarray from left to right is already sorted, the min is `nums[left]`.
Otherwise, we check the mid element.
If `nums[mid] >= nums[left]`, the left half is sorted, so the minimum must be in the right half.
Otherwise, the right half is sorted, so the minimum is in the left half (including mid).
"""
