from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        n = len(nums)
        
        while even < n and odd < n:
            while even < n and nums[even] % 2 == 0:
                even += 2
            while odd < n and nums[odd] % 2 != 0:
                odd += 2
                
            if even < n and odd < n:
                nums[even], nums[odd] = nums[odd], nums[even]
                
        return nums

"""
Approach:
Two pointers approach. `even` pointer tracks even indices, `odd` pointer tracks odd indices.
We advance `even` by 2 as long as the element at the even index is actually even.
We advance `odd` by 2 as long as the element at the odd index is actually odd.
When both stop, it means they are out of place, so we swap them.
"""
