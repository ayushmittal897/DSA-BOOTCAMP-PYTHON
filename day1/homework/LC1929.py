from typing import List
"""
Approach:
We need to create an array `ans` of length `2n` where `ans` is just `nums` repeated twice.
In Python, we can simply concatenate the list to itself.
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Concatenate the array with itself
        return nums + nums
