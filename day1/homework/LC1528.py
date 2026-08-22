from typing import List
"""
Approach:
We are given a string `s` and an array `indices` of the same length.
We want to move the character `s[i]` to the index `indices[i]`.
We can create a list of the same length to hold the characters in their correct positions,
then join them into a string.
"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create an empty list of the correct size
        shuffled = [''] * len(s)
        
        for i in range(len(s)):
            # Place the character at its target index
            target_index = indices[i]
            shuffled[target_index] = s[i]
            
        # Join the list back into a single string
        return "".join(shuffled)
