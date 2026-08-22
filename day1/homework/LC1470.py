from typing import List
"""
Approach:
The array contains 2n elements, alternating between x and y components.
We can create a new array and alternate adding elements from the first half (x) 
and the second half (y).
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        # Loop n times
        for i in range(n):
            # Append x_i
            result.append(nums[i])
            # Append y_i
            result.append(nums[i + n])
        return result
