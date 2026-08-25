from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
                
        return dp[amount]

"""
Approach:
Dynamic Programming (Unbounded Knapsack).
We use a 1D DP array where `dp[i]` represents the number of ways to make amount `i`.
We iterate over each coin, and for each coin, we update the DP array for all amounts 
greater than or equal to the coin's value. We accumulate the ways.
"""
