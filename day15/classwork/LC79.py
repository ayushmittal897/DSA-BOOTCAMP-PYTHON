from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or (r, c) in path):
                return False
                
            path.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            path.remove((r, c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False

"""
Approach:
Backtracking (DFS) on a grid.
We iterate through every cell in the grid. If the cell matches the first letter of our word, we start our DFS.
We use a `path` set to keep track of visited cells so we don't reuse them.
If we reach the end of the word (`i == len(word)`), we found it. We check all 4 adjacent directions recursively.
"""
