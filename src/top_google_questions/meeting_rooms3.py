"""
2
[[0,10],[1,5],[2,7],[3,4]]

3
[[1,20],[2,10],[3,5],[4,9],[6,8]]
"""
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_counts = [0] * n
        free = list(range(n))
        heapq.heapify(free)
        busy = []
        
        events = []
        for i, [start, end] in enumerate(meetings):
            heapq.heappush(events, [start, i])
            heapq.heappush(events, [end, i])
        
        current_time = 0
        
        while events:
            time, meeting_i = heapq.heappop(events)
            #print('time', time, 'meeting_i', meeting_i)
            
            current_time = max(time, current_time)
            self.clean_rooms(current_time, busy, free)

            # start
            if meetings[meeting_i][0] == time:
                if not free:
                    current_time = busy[0][0]
                    self.clean_rooms(current_time, busy, free)
                    
                room_i = heapq.heappop(free)
                room_counts[room_i] += 1
                heapq.heappush(busy, [meetings[meeting_i][1] - time + current_time, room_i])
                
            # end
            else:
                if current_time <= time:
                    current_time = time
                    self.clean_rooms(current_time, busy, free)
            
            #print(current_time, free, busy, room_counts)
        
        max_count = max(room_counts)
        for i in range(n):
            if max_count == room_counts[i]:
                return i
            
    def clean_rooms(self, current_time, busy, free):
        while busy and busy[0][0] <= current_time:
            _, room_i = heapq.heappop(busy)
            heapq.heappush(free, room_i)
