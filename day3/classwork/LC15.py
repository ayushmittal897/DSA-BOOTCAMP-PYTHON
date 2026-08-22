from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

"""
Approach:
Sort the array first. Iterate through the array with a pointer `i`.
For each `nums[i]`, use a two-pointer approach (`left` and `right`) for the remaining part of the array
to find pairs that sum up to `-nums[i]`.
Skip duplicates for `i`, `left` to avoid duplicate triplets.
"""
