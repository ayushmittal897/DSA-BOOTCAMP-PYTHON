from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 != 0:
                right -= 1
                
        return nums

"""
Approach:
Two pointers approach. `left` starts at 0, `right` starts at the end.
If `nums[left]` is odd and `nums[right]` is even, we swap them.
We increment `left` if it points to an even number, and decrement `right` if it points to an odd number.
This does it in-place in O(n) time.
"""
