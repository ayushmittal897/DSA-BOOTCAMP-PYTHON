from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        
        def backtrack(index, current_str):
            if index == len(digits):
                res.append(current_str)
                return
                
            for char in mapping[digits[index]]:
                backtrack(index + 1, current_str + char)
                
        backtrack(0, "")
        return res

"""
Approach:
We use backtracking to explore all possible letter combinations.
For each digit, we loop through its corresponding letters from the mapping.
We recursively add one letter at a time to our `current_str`.
When the length of `current_str` matches the length of `digits`, we've formed a valid combination.
"""
