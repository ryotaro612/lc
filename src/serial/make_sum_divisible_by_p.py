class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        found = {0: -1}
        result = n
        total = sum(nums) % p
        if total == 0:
            return 0
        cur = 0
        for i in range(n):
            cur += nums[i]
            cur %= p

            need = (cur - total + p) % p
            if need in found:
                result = min(result, i - found[need])

            found[cur] = i

        return -1 if result == n else result
