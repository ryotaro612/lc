"""
[1,-2,3,4,-10,12]
16

[1,-2,3,4,-10,12,9,12,2,3,4,6,7,0]
 16

[0,0,1,1,0,0,0,0,0,0,0,-1,-1,-1,0,0,0]
2

[-347135403,-741775723,349271195,967839234,822470265,-545249891,293401682,908306445,296832265,9392523,-84929173,-784997375,699878100,291656873,-910458294,547370160,584504507,977373244,-963031162,819184328]
473
"""
import heapq
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = sum([max(0, num) for num in nums])
        result = [max_sum]
        abs_nums = sorted([abs(num) for num in nums])
        
        heap = [(-max_sum + abs_nums[0], 0)]
        
        while len(result) < k:
            v, i = heapq.heappop(heap)
            heapq.heappush(result, -v)
            if i + 1 < n:
                heapq.heappush(heap, (v - abs_nums[i] + abs_nums[i+1], i+1))
                heapq.heappush(heap, (v + abs_nums[i+1], i+1))
        return result[0]
