from typing import List
"""
Approach:
We use a two-pointer approach. Initialize one pointer at the start (`left`) 
and one at the end (`right`). Swap the characters at these pointers, 
then move the pointers towards each other until they cross.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
