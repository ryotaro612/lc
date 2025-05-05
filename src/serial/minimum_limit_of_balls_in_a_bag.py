class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        lb = 0
        ub = max(nums) + 1
        cache = dict()
        while ub - lb > 1:
            mid = (ub + lb) // 2
            counter = 0
            
            for num in nums:
                # counter += self.count(num, mid, cache)
                counter += (num-1) // mid
            if counter > maxOperations:
                lb = mid
            else: # counter <= maxOperation
                ub = mid

        return ub
        
    
    def count(self, num, mid, cache):
        if num <= mid:
            return 0
        
        if num in cache:
            return cache[(num, mid)]

        
        if num % 2:
            cache[(num, mid)] = 1 + self.count(num // 2 + 1, mid, cache) + self.count(num // 2, mid, cache)
        else:
            cache[(num, mid)] = 1 + self.count(num // 2, mid, cache) * 2
        
        # num <= mid 0, num = mid + 1 => 1 num == 2*mid => 1 num == 2*mid + 1 => 2
        cache[(num, mid)] = min(cache[(num, mid)], (num-1) // mid)
         
        return cache[(num, mid)]
