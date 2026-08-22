from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

"""
Approach:
To rotate an array by `k` steps in O(1) space, we can use array reversals.
First, reverse the entire array.
Second, reverse the first `k` elements.
Finally, reverse the rest of the elements.
"""
