"""
[[1,2,7],[3,6,7]]
1
6

[[7,12],[4,5,15],[6],[15,19],[9,12,13]]
15
12
"""
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops = dict()
        stop_to_routes = dict()
        for i, route in enumerate(routes):
            for stop in route:
                stops.setdefault(stop, float('inf'))
                stop_to_routes.setdefault(stop, [])
                stop_to_routes[stop].append(i)
        
        if target not in stops:
            return -1
        stops[source] = 0
        que = deque()
        que.append((source, stops[source]))
        is_processed = [False] * len(routes)

        while len(que) > 0:
            stop, dist = que.popleft()
        
            if stops[stop] < dist:
                continue
                
            for route_idx in stop_to_routes[stop]:
                if is_processed[route_idx]:
                    continue
                else:
                    is_processed[route_idx] = True
                for arrival_stop in routes[route_idx]:
                    if stops[stop] + 1 < stops[arrival_stop]:
                        stops[arrival_stop] = stops[stop] + 1
                        que.append((arrival_stop, stops[arrival_stop]))
        if stops[target] == float('inf'):
            return -1
        else:
            return stops[target]
        
