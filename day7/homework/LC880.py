"""
Approach:
First, calculate the total length of the decoded string without actually building it.
Then, work backwards through the string.
If a character is a digit, we divide the current `length` by the digit.
Otherwise, we decrement `length` by 1.
Whenever `k % length == 0` and the current character is a letter, it means this letter is our answer.
"""
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for char in s:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1
                
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            k %= length
            
            if k == 0 and char.isalpha():
                return char
                
            if char.isdigit():
                length //= int(char)
            else:
                length -= 1
