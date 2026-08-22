from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            ships = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    ships += 1
                    curr_weight = w
                else:
                    curr_weight += w
            return ships <= days

        left, right = max(weights), sum(weights)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res

"""
Approach:
Binary search on the answer (the capacity of the ship).
The minimum capacity is the maximum weight (since we can't split a package).
The maximum capacity is the sum of all weights (shipping everything in 1 day).
We use binary search to find the minimum valid capacity that can ship within `days` days.
"""
