"""
Approach:
Every match played eliminates exactly one team. 
To get a single winner from `n` teams, exactly `n - 1` teams must be eliminated.
Therefore, exactly `n - 1` matches must be played. Time complexity: O(1).
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
