"""
[3,8,4,2,5,3,8,6]
1
"""
import heapq

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        heap = []

        n = len(nums)
        result = [True] * n
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            result[i] = False
        for i in range(k, n):
            result[i] = -heap[0] < nums[i]
            heapq.heappush(heap, -nums[i])
            heapq.heappop(heap)
        heap = []
        # print(result)
        for i in range(n-1, n-1-k, -1):
            heapq.heappush(heap, -nums[i])
            result[i] = False
        for i in range(n-1-k, -1, -1):
            # print(i, -heap[0], nums[i])
            result[i] = result[i] and -heap[0] < nums[i]
            heapq.heappush(heap, -nums[i])
            heapq.heappop(heap)
        # print(result)
        return len([e for e in result if e])
