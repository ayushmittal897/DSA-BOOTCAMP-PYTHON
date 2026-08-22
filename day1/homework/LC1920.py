from typing import List
"""
Approach:
We need to build a new array `ans` where `ans[i] = nums[nums[i]]`.
The simplest approach is to create a new array and populate it according to the rule.
"""
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            # Append the value at the index nums[i]
            ans.append(nums[nums[i]])
        return ans
