"""
Approach:
Simulate the elimination process without actually deleting elements.
Track the `head` of the remaining numbers, the distance between numbers (`step`), 
and the count of remaining numbers.
The `head` changes when moving left-to-right, OR when moving right-to-left and the remaining count is odd.
"""
class Solution:
    def lastRemaining(self, n: int) -> int:
        left_to_right = True
        remaining = n
        step = 1
        head = 1
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
                
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
            
        return head
