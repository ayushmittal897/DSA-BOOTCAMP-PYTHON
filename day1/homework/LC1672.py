from typing import List
"""
Approach:
We are given a 2D array where each row represents a customer and columns represent their bank accounts.
We want to find the maximum wealth (sum of all accounts for a customer).
We can iterate through each customer's accounts, calculate their total wealth, and keep track of the maximum.
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            # Calculate the total wealth for the current customer
            current_wealth = sum(customer)
            # Update the maximum wealth if the current is greater
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth
