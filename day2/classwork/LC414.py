from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for num in nums:
            if num in (first, second, third):
                continue
                
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
                
        return int(third) if third != float('-inf') else int(first)

"""
Approach:
We can keep track of the top three maximum numbers seen so far.
Initialize three variables to negative infinity.
For each number, if it is already one of the top three, skip it.
Otherwise, update the variables if it's larger than the current first, second, or third.
Finally, return the third max if it exists, else the first max.
"""
