class Solution:
    def maximumSubarraySum(self, nums, k):
        count = {}
        left = 0
        window_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > 1:
                count[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

                count[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1

        return max_sum
