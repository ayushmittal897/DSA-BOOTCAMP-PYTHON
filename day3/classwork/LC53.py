from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
            
        return max_sum

"""
Approach:
Kadane's Algorithm. We iterate through the array maintaining a running sum `cur_sum`.
If `cur_sum` becomes negative, it means it will only decrease any future sums, so we reset it to 0.
We keep track of the maximum `cur_sum` seen so far.
"""
