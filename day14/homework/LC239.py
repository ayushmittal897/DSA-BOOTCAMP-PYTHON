from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indices
        l = 0
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
                
        return res

"""
Approach:
Use a monotonically decreasing deque that stores indices.
The front of the deque will always have the index of the maximum element for the current window.
When adding a new element, remove all smaller elements from the back of the deque, since they will never be the maximum.
Remove the front element if its index is out of the current window bounds.
"""
