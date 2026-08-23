from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

"""
Approach:
Use a stack to keep track of the scores.
Iterate through the operations:
- For an integer, append it to the stack.
- For '+', add the sum of the last two scores.
- For 'D', double the last score and add it.
- For 'C', pop the last score.
Finally, return the sum of the stack.
"""
