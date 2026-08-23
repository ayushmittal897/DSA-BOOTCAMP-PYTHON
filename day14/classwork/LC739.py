from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
            
        return res

"""
Approach:
Use a monotonic decreasing stack that stores pairs of (temperature, index).
As we iterate through the temperatures, if we find a warmer day, we resolve the wait days for the cooler days stored on the stack.
The number of days is the difference between the current index and the popped index.
"""
