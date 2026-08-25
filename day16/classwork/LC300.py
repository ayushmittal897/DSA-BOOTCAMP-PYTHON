from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)

"""
Approach:
Patience Sorting / Binary Search (O(N log N)).
We maintain a `tails` array which stores the smallest tail of all increasing subsequences of length `i+1`.
For each number, we use binary search to find the position it should replace. 
If it's larger than all elements, it extends the longest subsequence.
"""
