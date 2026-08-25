from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                    
        return dp[0]

"""
Approach:
Dynamic Programming.
`dp[i]` stores whether the substring `s[i:]` can be segmented.
We iterate backwards. At index `i`, we check all words in `wordDict`. 
If a word matches `s[i:i+len]`, then `dp[i]` is True if `dp[i+len]` is True.
"""
