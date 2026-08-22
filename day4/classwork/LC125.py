"""
Approach:
Use two pointers, one at the beginning and one at the end.
Move the pointers inward, skipping any non-alphanumeric characters.
Compare the lowercase versions of the characters at the pointers.
If they mismatch, it's not a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
