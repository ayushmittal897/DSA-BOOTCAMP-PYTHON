from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))

"""
Approach:
Convert both arrays to sets to remove duplicates and enable O(1) lookups.
Then, simply find the intersection of the two sets.
Finally, convert the resulting set back to a list.
"""
