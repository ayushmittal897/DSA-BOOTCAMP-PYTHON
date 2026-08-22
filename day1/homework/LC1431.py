from typing import List
"""
Approach:
We want to find out if giving extra candies to each kid will make them have the most candies.
First, we find the maximum number of candies any kid currently has.
Then, we iterate through the list and check if `current_candies + extraCandies >= max_candies`.
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum candies currently held by any kid
        max_candies = max(candies)
        result = []
        
        for candy in candies:
            # Check if giving extra candies makes them have the greatest or equal to max
            result.append(candy + extraCandies >= max_candies)
            
        return result
