from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            
        return [1] + digits

"""
Approach:
We iterate backwards from the last digit.
If the digit is less than 9, we simply increment it by 1 and return the array.
If it is 9, it becomes 0 and we carry over 1 to the next iteration.
If we finish the loop (meaning all digits were 9), we prepend a 1 to the array.
"""
