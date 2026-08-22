from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        val = 1
        
        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = val
                val += 1
            top += 1
            
            for i in range(top, bottom):
                matrix[i][right - 1] = val
                val += 1
            right -= 1
            
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = val
                val += 1
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = val
                val += 1
            left += 1
            
        return matrix

"""
Approach:
Very similar to Spiral Matrix I.
We create an `n x n` matrix and define the boundaries.
We fill the cells with incrementally increasing values from 1 to `n^2` in a spiral pattern.
"""
