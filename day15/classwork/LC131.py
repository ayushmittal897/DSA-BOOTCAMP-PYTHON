from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(substring):
            return substring == substring[::-1]
            
        def backtrack(index, current_partition):
            if index == len(s):
                res.append(current_partition[:])
                return
                
            for i in range(index, len(s)):
                substring = s[index:i+1]
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(i + 1, current_partition)
                    current_partition.pop()
                    
        backtrack(0, [])
        return res

"""
Approach:
Backtracking. We want to find all palindrome partitions.
At any given `index`, we try creating a substring from `index` to `i`.
If this `substring` is a palindrome, it's a valid cut. We add it to our `current_partition` and recursively backtrack from `i + 1`.
If we reach the end of the string, we've found a complete valid partition.
"""
