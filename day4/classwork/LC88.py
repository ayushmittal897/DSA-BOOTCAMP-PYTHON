from typing import List
"""
Approach:
Since `nums1` has enough space at the end, we can use three pointers starting from the back.
`p1` points to the last actual element in `nums1`, `p2` points to the last in `nums2`.
`p` points to the very end of `nums1`. We compare and place the largest element at `p`.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
