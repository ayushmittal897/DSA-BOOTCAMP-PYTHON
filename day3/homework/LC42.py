from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res

"""
Approach:
Two pointers approach. The amount of water trapped at a position is dictated by `min(leftMax, rightMax) - height`.
Instead of computing leftMax and rightMax arrays, we can maintain them on the fly.
We move the pointer that points to the smaller max because the bottleneck is the smaller one.
"""
