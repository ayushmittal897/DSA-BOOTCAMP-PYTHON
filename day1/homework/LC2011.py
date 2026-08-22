from typing import List
"""
Approach:
We are given a list of operations that increment ("++X", "X++") or decrement ("--X", "X--") a variable X.
We can iterate through the operations and update X accordingly.
A simple trick is to check the middle character of the string: if it's '+', we add 1, if it's '-', we subtract 1.
"""
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            # The second character determines the operation
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x
