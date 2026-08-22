"""
Approach:
We want to find the sum of all integers in the range [1, n] that are divisible by 3, 5, or 7.
We can iterate through all numbers from 1 to n, and if a number is divisible by 3, 5, or 7, we add it to our total sum.
"""
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        for i in range(1, n + 1):
            # Check if divisible by 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total_sum += i
        return total_sum
