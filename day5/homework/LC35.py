from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left

"""
Approach:
Standard binary search. 
If the target is not found, the `left` pointer will end up pointing to the index
where the target should be inserted to maintain sorted order.
"""
