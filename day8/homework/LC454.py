class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        # Store sums of nums1 + nums2
        for a in nums1:
            for b in nums2:
                total = a + b
                count[total] = count.get(total, 0) + 1

        result = 0

        # Find sums of nums3 + nums4 that cancel them
        for c in nums3:
            for d in nums4:
                target = -(c + d)

                if target in count:
                    result += count[target]

        return result
