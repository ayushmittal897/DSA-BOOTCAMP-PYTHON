class Solution:
    def numberOfSubarrays(self, nums, k):
        count = {0: 1}
        odd = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                odd += 1

            if odd - k in count:
                result += count[odd - k]

            count[odd] = count.get(odd, 0) + 1

        return result
