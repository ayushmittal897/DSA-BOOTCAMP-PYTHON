from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[n - 1] = 1
        
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
                    
        return dp[0]

"""
Approach:
Dynamic Programming.
Similar to Unique Paths, but if there's an obstacle (1), the number of paths from that cell is 0.
We use a 1D DP array for space optimization, scanning backwards. 
For non-obstacle cells, `dp[c] = dp[c] (from below) + dp[c + 1] (from right)`.
"""
