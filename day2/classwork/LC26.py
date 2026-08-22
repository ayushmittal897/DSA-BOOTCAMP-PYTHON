from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        insert_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        return insert_index

"""
Approach:
Since the array is sorted, duplicates will be adjacent.
We use a two-pointer approach where `insert_index` tracks where to put the next unique element.
We iterate through the array, and whenever we see a new unique element (different from the previous),
we place it at `insert_index` and increment it.
"""
