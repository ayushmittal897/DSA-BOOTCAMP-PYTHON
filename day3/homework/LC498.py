from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []
        
        m, n = len(mat), len(mat[0])
        res = []
        r, c = 0, 0
        up = True
        
        for _ in range(m * n):
            res.append(mat[r][c])
            if up:
                if c == n - 1: r += 1; up = False
                elif r == 0: c += 1; up = False
                else: r -= 1; c += 1
            else:
                if r == m - 1: c += 1; up = True
                elif c == 0: r += 1; up = True
                else: r += 1; c -= 1
                
        return res

"""
Approach:
Simulate the traversal. Keep track of direction (up or down).
When moving up, we decrease row and increase col. If we hit the top or right boundary, we change direction.
When moving down, we increase row and decrease col. If we hit the bottom or left boundary, we change direction.
"""
