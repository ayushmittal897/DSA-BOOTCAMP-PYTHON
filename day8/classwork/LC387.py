class Solution:
    def firstUniqChar(self, s):
        count = {}

        # Count characters
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Find first character with count = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
