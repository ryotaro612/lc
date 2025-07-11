import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)

        heap = [-num for num in nums]
        heapq.heapify(heap)
        cur_sum = total
        result = 0
        while cur_sum * 2 > total:
            v = heapq.heappop(heap)
            v = -v
            cur_sum -= v / 2
            heapq.heappush(heap, -v / 2)
        
            result += 1
        
        return result
