from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def countNeighbors(r, c):
            nei = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei
            
        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbors(r, c)
                if board[r][c] == 1 and nei in [2, 3]:
                    board[r][c] = 3
                elif board[r][c] == 0 and nei == 3:
                    board[r][c] = 2
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

"""
Approach:
To do this in-place, we use states to track transitions:
0: dead -> dead, 1: live -> dead, 2: dead -> live, 3: live -> live.
When counting neighbors, 1 and 3 mean the cell was originally alive.
After processing, we map the states back to 0 or 1.
"""
