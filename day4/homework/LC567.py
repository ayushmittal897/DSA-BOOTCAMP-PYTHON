import collections
"""
Approach:
Use a sliding window of fixed size (length of s1) over s2.
We keep a frequency map of characters in s1, and another for the current window in s2.
As we slide the window, we add the new character to the window map and remove the old one.
If the maps match at any point, s2 contains a permutation of s1.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = collections.Counter(s1)
        window_count = collections.Counter(s2[:len(s1)])
        
        if s1_count == window_count:
            return True
            
        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            new_char = s2[i]
            
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char]
                
            window_count[new_char] += 1
            
            if s1_count == window_count:
                return True
                
        return False
