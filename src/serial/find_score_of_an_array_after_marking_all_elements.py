import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        []
        heap = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(heap)

        score = 0
        consumed = set()
        while heap:
            num, i = heapq.heappop(heap)

            if i in consumed:
                continue
            
            score += num
            consumed.add(i-1)
            consumed.add(i+1)
            consumed.add(i)
        
        return score
