import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pos = startFuel
        station_i = 0
        result = 0
        n_station = len(stations)
        heap = []
        while pos < target:
            while station_i < n_station and stations[station_i][0] <= pos:
                heapq.heappush(heap, -stations[station_i][1])
                station_i += 1
            
            if heap:
                pos -= heapq.heappop(heap)
                result += 1
            else:
                return -1
        return result
