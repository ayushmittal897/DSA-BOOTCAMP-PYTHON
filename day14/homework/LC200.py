from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r_new, c_new = row + dr, col + dc
                    if (r_new in range(rows) and 
                        c_new in range(cols) and 
                        grid[r_new][c_new] == "1"):
                        grid[r_new][c_new] = "0"
                        q.append((r_new, c_new))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
                    
        return islands

"""
Approach:
Iterate through the grid. When we find a "1" (land), we found a new island.
We then use Breadth-First Search (BFS) with a queue to explore all connected land components.
To prevent infinite loops and avoid revisiting, we mark visited land cells as "0" (water).
"""
