"""
Approach:
Use a stack to build the decoded string. Iterate through each character:
- Digits build the repetition `k`.
- '[' pushes the current accumulated string and `k` onto the stack, and resets them.
- ']' pops the last string and `k` from the stack, and appends the current string repeated `k` times.
- Letters simply append to the current string.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += char
                
        return curr_str
