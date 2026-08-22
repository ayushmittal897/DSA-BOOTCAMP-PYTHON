"""
Approach:
An anagram must have the exact same length and same character frequencies.
We can use a hash map (or Counter) to count frequencies, or simply sort the strings.
Sorting takes O(N log N), while counting takes O(N).
"""
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
