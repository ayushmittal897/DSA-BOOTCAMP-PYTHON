from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

"""
Approach:
Standard Binary Search algorithm.
We repeatedly check the middle element of the search space.
If it matches, return its index. If it's too small, search the right half.
If it's too large, search the left half.
"""
