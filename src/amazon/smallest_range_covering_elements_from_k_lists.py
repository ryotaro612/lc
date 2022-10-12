# n log (k)
import heapq
from collections import deque

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k = len(nums)
        
        heap = []
        rev_heap = []
        consumed = dict()
        
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            heapq.heappush(rev_heap, (-nums[i][0], -i, 0))
        
        index = [1] * k
        
        result = []
        while True:
            left = heap[0][0]
            while (-rev_heap[0][1], -rev_heap[0][2]) in consumed:
                heapq.heappop(rev_heap)
                
            right = -rev_heap[0][0]
            if result == [] or right - left < result[1] - result[0] or left < result[0]:
                result = [left, right]
            
            _, i, j = heapq.heappop(heap)
            consumed[(i, j)] = True
            
            if index[i] < len(nums[i]):
                heapq.heappush(heap, (nums[i][index[i]], i, index[i]))
                heapq.heappush(rev_heap, (-nums[i][index[i]], -i, -index[i]))
                index[i] += 1
            else:
                return result
