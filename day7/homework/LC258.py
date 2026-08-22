"""
Approach:
The digital root of a non-negative integer `num` can be found in O(1) time.
Using the property of numbers base 10, any number `num` modulo 9 gives the sum of its digits modulo 9.
If `num` is a multiple of 9 (and > 0), the digital root is 9.
This can be summarized by the formula: 1 + (num - 1) % 9.
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
