from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

"""
Approach:
We want to buy at the lowest possible price and sell at the highest possible price after buying.
We iterate through the prices while keeping track of the minimum price seen so far.
At each step, we calculate the potential profit if we sold today, and update the maximum profit if it's higher.
"""
