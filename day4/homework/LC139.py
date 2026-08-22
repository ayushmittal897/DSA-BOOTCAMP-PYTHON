from typing import List
"""
Approach:
Use Dynamic Programming. `dp[i]` indicates whether `s[:i]` can be segmented 
using words from the dictionary. We iterate over lengths `i` from 1 to len(s).
For each `i`, we check if there exists a `j < i` such that `dp[j]` is True 
and `s[j:i]` is a valid word.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[-1]
