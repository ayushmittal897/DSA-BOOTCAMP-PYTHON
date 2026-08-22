"""
Approach:
Sliding window using two pointers (`left` and `right`) and a set for seen characters.
Expand the `right` pointer. If the character is already in the set, 
shrink the window from the `left` until the duplicate is removed.
Keep track of the maximum window size seen.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len
