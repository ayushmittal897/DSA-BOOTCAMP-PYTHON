class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}
        prefix = 0
        longest = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in first:
                longest = max(longest, i - first[prefix])
            else:
                first[prefix] = i

        return longest
