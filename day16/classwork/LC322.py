from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

"""
Approach:
Dynamic Programming (Bottom-Up).
We create a `dp` array where `dp[i]` is the minimum coins needed to make amount `i`.
We initialize with `amount + 1` (infinity).
For each amount, we check every coin to see if taking it results in a smaller coin count.
"""
