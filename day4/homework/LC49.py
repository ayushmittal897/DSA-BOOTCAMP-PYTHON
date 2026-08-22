import collections
from typing import List
"""
Approach:
Two words are anagrams if their sorted versions are identical.
We can use a hash map where the key is the sorted word as a tuple of characters,
and the value is the list of original words that match that sorted key.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            groups[tuple(sorted(word))].append(word)
        return list(groups.values())
