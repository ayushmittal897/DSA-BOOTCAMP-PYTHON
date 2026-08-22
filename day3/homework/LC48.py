from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                
                topLeft = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft
                
            right -= 1
            left += 1

"""
Approach:
Rotate layer by layer (outer to inner).
For each layer, save the top-left element, and perform a 4-way swap of the corners/edges.
You can also solve this by transposing the matrix and then reversing each row.
"""
