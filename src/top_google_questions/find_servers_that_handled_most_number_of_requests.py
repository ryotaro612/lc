import heapq
"""
3
[1,2,3,4,5]
[5,2,3,3,3]

3
[1,2,3,4]
[1,2,1,2]

3
[1,2,3]
[10,12,11]
"""
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))
        busy = []
        
        counter = [0] * k
        
        for i in range(len(arrival)):
            
            while busy and busy[0][0] <= arrival[i]:
                _, free_id = heapq.heappop(busy)
                heapq.heappush(free, i + (free_id - i) % k)
            
            if free:
                busy_id = heapq.heappop(free) % k
                counter[busy_id] += 1
                
                heapq.heappush(busy, (arrival[i] + load[i], busy_id))
                
        max_count = max(counter)
            
        return [i for i, c in enumerate(counter) if c == max_count]
    
