from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

"""
Approach:
We use the XOR bitwise operation. 
XORing a number with itself results in 0 (e.g., A ^ A = 0).
XORing a number with 0 results in the number itself (e.g., A ^ 0 = A).
Since every number except one appears exactly twice, XORing all the numbers together 
will cancel out the pairs, leaving only the single number that appears once.
This gives us an O(N) time complexity and O(1) space complexity solution.
"""
