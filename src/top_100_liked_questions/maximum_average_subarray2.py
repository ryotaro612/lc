class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        lb = min(nums) - 1
        ub = max(nums) + 1
        
        prev_mid = float('inf')
        mid = 0
        while abs(mid - prev_mid) > 0.00001:
            prev_mid = mid
            mid = (lb + ub) / 2
            # print(mid)
            if self.check(nums, mid, k):
                lb = mid
            else:
                ub = mid
        return ub

    def check(self, nums, mid, k):
        nums = [num - mid for num in nums]
        
        n = len(nums)
        
        window = 0
        for i in range(k):
            window += nums[i]
            
        if window > 0:
            return True
        
        smallest = 0
        prev = 0
        for i in range(k, n):
            window += nums[i]
            
            
            prev += nums[i-k]
            smallest = min(smallest, prev)
        
            if window - smallest > 0:
                return True
            
        return False
