from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

"""
Approach:
Since the array is sorted, we can use a two-pointer approach.
Initialize pointers at the start and end of the array.
If the sum is greater than the target, move the right pointer left.
If the sum is less than the target, move the left pointer right.
"""
