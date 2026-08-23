from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+': stack.append(a + b)
                elif t == '-': stack.append(a - b)
                elif t == '*': stack.append(a * b)
                else: stack.append(int(a / b))  # Truncates toward zero
        return stack[0]

"""
Approach:
Use a stack to evaluate postfix expressions.
Iterate through the tokens. If it's a number, push it onto the stack.
If it's an operator, pop the top two numbers, apply the operation, and push the result back onto the stack.
"""
