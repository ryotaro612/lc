class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
        left, right = 0
        """
        result = set()
        n = len(nums)
        b = 10**9+7
        h = 1<<64
        for left in range(n):
            cnt = 0
            acc = 0 
            for right in range(left, n):
                cnt += 0 if nums[right] % p else 1
                if cnt <= k:
                    acc = (acc * b + nums[right]) % h
                    result.add(acc)
                else:
                    break
            
        return len(result)
