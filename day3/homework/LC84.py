from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area

"""
Approach:
Use a monotonic increasing stack to keep track of heights and the starting index where that height is valid.
When we see a smaller height, we pop from the stack and compute the area for those popped heights.
At the end, calculate areas for any remaining heights in the stack spanning to the end of the array.
"""
