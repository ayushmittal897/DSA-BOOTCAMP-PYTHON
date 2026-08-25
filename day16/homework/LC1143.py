class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[0][0]

"""
Approach:
Dynamic Programming (2D Grid).
We create a 2D DP table. If characters match, we take `1 + diagonal` value.
If they don't match, we take the max of the right cell (skip char in text2) 
or the bottom cell (skip char in text1). We build this bottom-up.
"""
