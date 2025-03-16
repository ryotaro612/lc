import heapq

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        heap = []
        for i, rank in enumerate(ranks):
            heapq.heappush(heap, (rank, i, 0))
        
        result = 0
        for _ in range(cars):
            time, i, meca_n_cars = heapq.heappop(heap)
            result = max(result, time)
        
            meca_n_cars += 1
            heapq.heappush(heap, (ranks[i] * ((meca_n_cars + 1)**2), i, meca_n_cars))
        

        return result
