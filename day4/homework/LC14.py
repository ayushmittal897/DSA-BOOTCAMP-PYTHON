from typing import List
"""
Approach:
If we sort the list of strings, the strings with the most differences will be 
at the first and last positions. We only need to find the common prefix 
between the first string and the last string in the sorted list.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]
