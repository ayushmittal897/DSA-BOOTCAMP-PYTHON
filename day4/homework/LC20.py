"""
Approach:
Use a stack to keep track of opening brackets. 
When a closing bracket is encountered, pop from the stack and verify it matches.
If it doesn't match or the stack is empty, return False.
At the end, return True if the stack is completely empty.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
                
        return not stack
