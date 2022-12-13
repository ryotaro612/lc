class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        mini = min(nums)
        maxi = max(nums)
        n = len(nums)
        size = max(1, (maxi - mini) // (n-1))
        buckets = [[None, None] for _ in range((maxi - mini)//size + 1)]
        
        for num in nums:
            i = (num - mini) // size
            if buckets[i][0] is None:
                buckets[i][0] = num
                buckets[i][1] = num
            else:
                buckets[i][0] = min(buckets[i][0], num)
                buckets[i][1] = max(buckets[i][1], num)
        
        result = 0
        prev_bucket = None
        for bucket in buckets:
            if bucket[0] is None:
                continue
            elif prev_bucket is None:
                prev_bucket = bucket
                continue
            else:
                result = max(result, bucket[0] - prev_bucket[1])
                prev_bucket = bucket
        return result
