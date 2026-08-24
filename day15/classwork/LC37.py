from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, num):
            for i in range(9):
                if board[r][i] == num: return False
                if board[i][c] == num: return False
                
            start_r, start_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_r + i][start_c + j] == num:
                        return False
            return True
            
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False # If no number 1-9 works, this path is dead
            return True # Board is fully filled
            
        backtrack()

"""
Approach:
Backtracking. We iterate through every cell on the board.
If a cell is empty ('.'), we try placing numbers '1' through '9'.
We have an `is_valid` helper to check if placing the number violates Sudoku rules (checking row, col, and 3x3 sub-box).
If it's valid, we place it and recurse. If the recursion returns False, we backtrack and reset the cell to '.'.
"""
