from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, find_left):
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    res = mid
                    if find_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res
            
        left_idx = binary_search(nums, target, True)
        right_idx = binary_search(nums, target, False)
        
        return [left_idx, right_idx]

"""
Approach:
We perform two binary searches.
First, we search for the leftmost index by continuing our search to the left even when we find the target.
Second, we search for the rightmost index by continuing our search to the right when we find the target.
"""
