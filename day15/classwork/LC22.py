from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, close_count, current_str):
            if open_count == n and close_count == n:
                res.append(current_str)
                return
                
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res

"""
Approach:
Backtracking. We keep track of the number of opening and closing brackets we have used.
We can add an opening bracket '(' if we haven't reached `n` opening brackets yet.
We can add a closing bracket ')' only if the count of closing brackets is strictly less than the count of opening brackets (to ensure validity).
When both counts reach `n`, we add the string to the result.
"""
