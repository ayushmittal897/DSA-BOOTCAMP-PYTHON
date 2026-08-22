from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 2
                
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
                    
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        return n + 1

"""
Approach:
We can use the array itself as a hash map. 
First, replace all negative numbers or zeros with `n + 2`.
Second, iterate through the array and use the magnitude of each value as an index `val - 1`
and negate the element at that index to mark it as "seen".
Finally, find the first index that contains a positive value; that index + 1 is the missing positive.
"""
