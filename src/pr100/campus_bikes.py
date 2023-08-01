import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)
        used_bikes = [False] * m
        patterns = [[abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), i, j] 
                    for i, worker in enumerate(workers)
                    for j, bike in enumerate(bikes)]
        patterns.sort()
        result = [None] * n
        for _, i_worker, i_bike in patterns:
            if result[i_worker] is None and not used_bikes[i_bike]:
                result[i_worker] = i_bike
                used_bikes[i_bike] = True
        return result
        
