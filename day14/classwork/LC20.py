class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

"""
Approach:
We use a stack to keep track of opening brackets.
When we encounter a closing bracket, we check if it matches the top of the stack.
If it matches, we pop the top element. Otherwise, it's invalid.
At the end, if the stack is empty, it means all brackets were closed properly.
"""
