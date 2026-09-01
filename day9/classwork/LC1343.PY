class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        count = 0

        # First window
        window_sum = sum(arr[:k])

        if window_sum >= target:
            count += 1

        # Slide the window
        for i in range(k, len(arr)):
            window_sum += arr[i]       # add new element
            window_sum -= arr[i - k]   # remove old element

            if window_sum >= target:
                count += 1

        return count
