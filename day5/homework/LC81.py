from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
                
            # If we have duplicates, we might not know which half is sorted
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
                
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False

"""
Approach:
Similar to Search in Rotated Sorted Array I, but with duplicates.
When `nums[left] == nums[mid] == nums[right]`, we can't reliably determine which half is sorted.
In that case, we simply shrink our search space by moving both pointers inwards by 1.
"""
