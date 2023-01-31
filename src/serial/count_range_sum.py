import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum =set()
        total = 0
        for num in nums:
            total += num
            prefix_sum.add(total)
        prefix_sum = sorted(prefix_sum)
        sum_to_i = {v: i for i, v in enumerate(prefix_sum)}

        bit = [0] * (len(prefix_sum) + 1)
        total = 0
        for num in nums:
            total += num
            i = sum_to_i[total]
            self.add(bit, i, 1)
    
        result = 0
        total = 0
        for i, num in enumerate(nums):
            left = bisect.bisect_left(prefix_sum, total + lower)
            right = bisect.bisect_right(prefix_sum, total + upper)
            result += self.sum(bit, right-1)
            if left:
                result -= self.sum(bit, left-1)
            
            total += num
            self.add(bit, sum_to_i[total], -1)            

        return result
        
    def add(self, bit, i, v):
        n = len(bit)
        i += 1
        while i < n:
            bit[i] += v
            i += i & -i
    
    def sum(self, bit, i):
        result = 0
        i += 1
        while i:
            result += bit[i]
            i -= i & -i
        return result
