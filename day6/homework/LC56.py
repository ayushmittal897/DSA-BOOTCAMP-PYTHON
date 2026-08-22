from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_merged = merged[-1]
            current = intervals[i]
            
            if current[0] <= last_merged[1]:
                # Overlapping intervals, update the end if necessary
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval
                merged.append(current)
                
        return merged

"""
Approach:
First, sort the intervals based on their start times.
Initialize a list `merged` with the first interval.
Iterate through the rest of the intervals. If the current interval overlaps with the last one in `merged`,
update the end time of the last interval to be the maximum of the two end times.
Otherwise, they don't overlap, so append the current interval to `merged`.
"""
