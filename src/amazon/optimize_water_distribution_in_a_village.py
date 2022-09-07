import heapq
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        have_water = [False] * n
        
        heap = []
        for i, well in enumerate(wells):
            heapq.heappush(heap, (well, i))
        g = [[] for _ in range(n)]
        for house1, house2, cost in pipes:
            g[house1-1].append((house2-1, cost))
            g[house2-1].append((house1-1, cost))
        
        result = 0
        while heap:
            cost, house = heapq.heappop(heap)
            if have_water[house]:
                continue
            result += cost
            have_water[house] = True
            
            for other, cost in g[house]:
                if have_water[other] is False:
                    heapq.heappush(heap, (cost, other))
            
        return result
