from typing import List
"""
Approach:
We are given an array of sentences and need to find the maximum number of words in a single sentence.
Words are separated by spaces. The number of words is exactly the number of spaces + 1.
We can just count the spaces in each sentence or split the sentence by space and get the length.
"""
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            # Split the sentence by space to get a list of words
            words = sentence.split(" ")
            # Update max_words if this sentence has more words
            if len(words) > max_words:
                max_words = len(words)
        return max_words
