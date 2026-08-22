from typing import List
"""
Approach:
We need to count how many numbers in the array have an even number of digits.
We can convert each number to a string and check if its length is even.
This is a very simple and readable approach.
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            # Convert number to string to easily get the number of digits
            if len(str(num)) % 2 == 0:
                even_count += 1
        return even_count
