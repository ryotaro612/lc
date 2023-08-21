class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        buckets = [[] for _ in range(k)]
        nums = sorted(nums)
        for num in nums:
            buckets[num % k].append(num)
        
        res = 1
        for bucket in buckets:
            bn = len(bucket)
            sub, prev = 1, 1
            for i in range(bn):
                if i and bucket[i] - bucket[i-1] == k:
                    cur = sub - prev
                else:
                    cur = sub
                sub += cur
                prev = cur
            res *= sub
        return res
