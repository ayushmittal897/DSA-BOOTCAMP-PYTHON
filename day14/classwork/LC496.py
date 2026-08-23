from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        while stack:
            next_greater[stack.pop()] = -1
            
        return [next_greater[num] for num in nums1]

"""
Approach:
Use a monotonic decreasing stack to find the next greater element for all items in `nums2`.
We iterate through `nums2`. If we see a larger number than the top of our stack, it is the next greater element for the items on the stack.
We use a hash map to store these mappings for O(1) lookups when processing `nums1`.
"""
