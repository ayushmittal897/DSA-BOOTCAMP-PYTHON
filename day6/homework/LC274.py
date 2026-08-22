from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h

"""
Approach:
Sort the citations in descending order.
Iterate through the sorted array. If the citation count at index `i` is at least `i + 1`, 
it means the researcher has at least `i + 1` papers with `i + 1` or more citations.
We update our h-index and continue. We break when this condition fails.
"""
