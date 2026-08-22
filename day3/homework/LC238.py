from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

"""
Approach:
First pass: compute the prefix products and store them in the result array.
Second pass: compute the postfix products on the fly and multiply them into the result array.
This avoids using division and runs in O(n) time with O(1) extra space.
"""
