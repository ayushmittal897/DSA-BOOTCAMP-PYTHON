from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
                
        return res

"""
Approach:
Use a monotonic decreasing stack storing indices.
Since the array is circular, we can simulate traversing it twice by looping to `2*n` and using modulo `i % n`.
This allows elements at the end of the array to find their next greater element at the beginning of the array.
"""
