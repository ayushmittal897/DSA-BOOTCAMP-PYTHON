class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

"""
Approach:
We use a stack to process the string character by character.
If the current character is the same as the top of the stack, it's a duplicate pair, so we pop the top character.
Otherwise, we push the current character onto the stack.
The remaining characters in the stack form the final string.
"""
