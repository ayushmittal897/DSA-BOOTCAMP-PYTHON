class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
            
        return row[0]

"""
Approach:
Dynamic Programming.
A robot can only move right or down. To reach any cell, the number of paths is the sum of paths 
from the cell to its right and the cell below it.
We optimize space by keeping track of only a single row at a time, calculating from the destination backwards.
"""
