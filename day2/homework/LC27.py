from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        return insert_index

"""
Approach:
We use a two-pointer approach similar to removing duplicates.
`insert_index` tracks where the next valid element should be placed.
We iterate through the array, and if the current element is not `val`,
we copy it to the `insert_index` and increment `insert_index`.
"""
